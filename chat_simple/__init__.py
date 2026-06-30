from otree.api import *
from os import environ
from openai import AsyncOpenAI
import random
import json
from datetime import datetime, timezone

from study_progress import global_progress

doc = """
Humble AI Experiment - two conditions: Humble vs. Control AI
"""

author = 'adapted from Clint McKenna clint@calsocial.org'

########################################################
# Constants                                            #
########################################################
from .prompts import SYS_CONTROL as _SYS_CONTROL, SYS_HUMBLE as _SYS_HUMBLE, SYS_HUMBLE_EN

class C(BaseConstants):
    NAME_IN_URL = 'chat_simple'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    SHOW_HISTORY = True

    BOT_LABEL = 'AI Assistant'
    BOT_TEMP = 1.0

    OPENAI_KEY = environ.get('OPENAI_KEY')
    MODEL = "gpt-4.1-mini"

    SYS_CONTROL = _SYS_CONTROL
    SYS_HUMBLE  = _SYS_HUMBLE

########################################################
# LLM Setup                                            #
########################################################

async def runGPT(inputMessage):
    client = AsyncOpenAI(api_key=C.OPENAI_KEY)
    response = await client.chat.completions.create(
        model=C.MODEL,
        temperature=C.BOT_TEMP,
        max_tokens=300,
        messages=inputMessage,
        stream=False,
    )
    return response.choices[0].message.content


########################################################
# Models                                               #
########################################################

class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    players = subsession.get_players()

    conditions = ['Control', 'Humble']
    for p in players:
        condition = random.choice(conditions)
        p.condition = condition
        p.participant.condition = condition

        if condition == 'Control':
            sysPrompt = {'role': 'system', 'content': C.SYS_CONTROL}
        else:
            sysPrompt = {'role': 'system', 'content': C.SYS_HUMBLE}

        p.cachedMessages = json.dumps([sysPrompt])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    condition = models.StringField()
    cachedMessages = models.LongStringField(initial='[]')


########################################################
# Extra models                                         #
########################################################

class MessageData(ExtraModel):
    player = models.Link(Player)
    condition = models.StringField()
    msgId = models.StringField()
    timestamp = models.StringField()
    sender = models.StringField()
    fullText = models.StringField()
    msgText = models.StringField()


########################################################
# Custom export                                        #
########################################################

def custom_export(players):
    yield [
        'sessionId',
        'subjectId',
        'condition',
        'msgId',
        'timestamp',
        'sender',
        'fullText',
        'msgText',
    ]
    mData = MessageData.filter()
    for m in mData:
        player = m.player
        participant = player.participant
        session = player.session
        try:
            fullText = json.loads(m.fullText)
        except:
            fullText = m.fullText
        yield [
            session.code,
            participant.code,
            m.condition,
            m.msgId,
            m.timestamp,
            m.sender,
            fullText,
            m.msgText,
        ]


########################################################
# Pages                                                #
########################################################

class chat(Page):
    form_model = 'player'
    timeout_seconds = 300

    @staticmethod
    def js_vars(player):
        return dict(
            typing_delay_ms=1000,
            min_typing_ms=2000,
        )

    @staticmethod
    def vars_for_template(player):
        condition = player.condition
        if condition == 'Humble':
            botClass = 'blueText'
        else:
            botClass = 'blueText'
        cached = player.cachedMessages
        if cached and cached != '[]':
            cached_messages = json.loads(cached)
        else:
            cached_messages = []
        return dict(
            show_history=C.SHOW_HISTORY,
            botClass=botClass,
            cached_messages=cached_messages,
            condition=condition,
            progress=global_progress(12),
        )

    @staticmethod
    async def live_method(player: Player, data):

        if not data:
            yield {player.id_in_group: dict(
                messages=json.loads(player.cachedMessages),
            )}
            return

        messages = json.loads(player.cachedMessages)
        currentPlayer = 'P' + str(player.id_in_group)
        condition = player.condition

        if condition == 'Humble':
            botClass = 'blueText'
        else:
            botClass = 'blueText'

        if 'event' in data:
            event = data['event']

            if event == 'text':
                dateNow = str(datetime.now(tz=timezone.utc).timestamp())
                msgId = currentPlayer + '-' + str(dateNow)
                text = data['text']
                inputMsg = {'role': 'user', 'content': text}

                MessageData.create(
                    player=player,
                    condition=condition,
                    msgId=msgId,
                    timestamp=dateNow,
                    sender='Subject',
                    fullText=json.dumps(inputMsg),
                    msgText=text,
                )

                messages.append(inputMsg)
                player.cachedMessages = json.dumps(messages)

                yield {player.id_in_group: dict(
                    event='text',
                    selfText=text,
                    sender=currentPlayer,
                    botClass=botClass,
                    msgId=msgId,
                )}
                return

            elif event == 'botMsg':
                botId = C.BOT_LABEL
                dateNow = str(datetime.now(tz=timezone.utc).timestamp())
                botMsgId = botId + '-' + str(dateNow)
                
                # run GPT call
                botText = await runGPT(messages)
                
                # reload player from database after async call
                player = Player.objects_get(id=player.id)
                
                # create bot message
                botMsg = {'role': 'assistant', 'content': botText}
                
                MessageData.create(
                    player=player,
                    condition=player.condition,
                    msgId=botMsgId,
                    timestamp=dateNow,
                    sender=botId,
                    fullText=json.dumps(botMsg),
                    msgText=botText,
                )
                
                messages.append(botMsg)
                player.cachedMessages = json.dumps(messages)
                
                yield {player.id_in_group: dict(
                    event='botText',
                    sender=botId,
                    botMsgId=botMsgId,
                    text=botText,
                    botClass=player.condition,
                )}
                return


page_sequence = [
    chat,
]