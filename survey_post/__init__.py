from otree.api import *
from study_progress import global_progress

doc = """
Survey administered after the chat interaction.
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey_post'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # ── Verification Intention ──────────────────────────
    verif_intent_1 = models.IntegerField(
        label="Would you like to verify the information you received from the AI chatbot with additional sources?",
        choices=[[1, 'yes'], [0, 'no']], widget=widgets.RadioSelect)
    verif_intent_2 = models.IntegerField(
        label="Would you still like to see additional sources on this topic now?",
        choices=[[1, 'yes'], [0, 'no']], widget=widgets.RadioSelect)

    # ── Perceived Credibility (Appelman & Sundar) ───────
    # 1 = very poorly, 7 = very well
    cred_accurate = models.IntegerField(
        label="accurate", choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    cred_authentic = models.IntegerField(
        label="authentic", choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    cred_believable = models.IntegerField(
        label="believable", choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)

    # ── Perceived Uncertainty (Van Der Bles et al.) ─────
    uncert_1 = models.IntegerField(
        label="To what extent do you think the information you received about social media bans is certain or uncertain?",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    uncert_2 = models.IntegerField(
        label="How much uncertainty do you think there is about social media bans?",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    uncert_3 = models.IntegerField(
        label="After this search, how uncertain do you feel about this topic?",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)

    # ── Subjective Knowledge Sufficiency (post) ─────────
    know_post = models.IntegerField(
        label="How much do you feel you know about social media bans for children and adolescents under 16?",
        min=0, max=100)
    suff_post = models.IntegerField(
        label="How much would you need to know about this topic to feel sufficiently informed?",
        min=0, max=100)

    # ── Perceived Completeness ──────────────────────────
    # 1 = strongly disagree, 7 = strongly agree
    complete_1 = models.IntegerField(
        label="I am confident the AI's answers covered all the important aspects of social media bans.",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    complete_2 = models.IntegerField(
        label="The AI's responses gave me the complete picture on social media bans.",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    complete_3 = models.IntegerField(
        label="There are probably important aspects of social media bans the AI did not mention.",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)

    # ── Specific Intellectual Humility Scale (SIHS), last 3 items ──
    # 1 = not at all like me, 5 = very much like me
    sihs_7 = models.IntegerField(
        label="My views about social media bans today may someday turn out to be wrong.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    sihs_8 = models.IntegerField(
        label="When it comes to my views about social media bans I may be overlooking evidence.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    sihs_9 = models.IntegerField(
        label="My views about social media bans may change with additional evidence or information.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # ── Trait-level Intellectual Humility (GIHS, post) ──
    gihs_post_1 = models.IntegerField(
        label="I question my own opinions, positions, and viewpoints because they could be wrong.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    gihs_post_2 = models.IntegerField(
        label="I reconsider my opinions when presented with new evidence.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    gihs_post_3 = models.IntegerField(
        label="I recognize the value in opinions that are different from my own.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    gihs_post_4 = models.IntegerField(
        label="I accept that my beliefs and attitudes may be wrong.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    gihs_post_5 = models.IntegerField(
        label="In the face of conflicting evidence, I am open to changing my opinions.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    gihs_post_6 = models.IntegerField(
        label="I like finding out new information that differs from what I already think is true.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # ── Perceived AI Competence ──────────────────────────
    # 1 = strongly disagree, 5 = strongly agree
    comp_1 = models.IntegerField(
        label="knowledgeable", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    comp_2 = models.IntegerField(
        label="competent", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    comp_3 = models.IntegerField(
        label="capable", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # ── Perceived AI Warmth ──────────────────────────────
    warm_1 = models.IntegerField(
        label="warm", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    warm_2 = models.IntegerField(
        label="friendly", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    warm_3 = models.IntegerField(
        label="personal", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # ── Perceived AI Intellectual Humility ──────────────
    aih_1 = models.IntegerField(
        label="acknowledged uncertainty", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    aih_2 = models.IntegerField(
        label="considered alternative viewpoints", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    aih_3 = models.IntegerField(
        label="presented its answer as definitive", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    aih_4 = models.IntegerField(
        label="recognized its own knowledge limitations", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    aih_5 = models.IntegerField(
        label="admitted when it did not know something", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    aih_6 = models.IntegerField(
        label="expressed the fallibility of knowledge", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # ── Naturality of the Search Environment and Workflow ──
    natural_similar = models.IntegerField(
        label="How similar was the interaction with this AI chatbot to AI chatbots you are familiar with (e.g., ChatGPT)?",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    natural_feel = models.IntegerField(
        label="How natural did the interaction with the AI chatbot feel?",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    natural_open = models.LongStringField(
        label="If anything felt different, please describe it briefly:", blank=True)

    # ── Post Attitude ────────────────────────────────────
    attitude_post = models.IntegerField(
        label="Banning social media for children and adolescents under the age of 16 is the right thing to do.",
        choices=[1, 2, 3, 4, 5, 6], widget=widgets.RadioSelectHorizontal)


########################################################
# Pages                                                #
########################################################

class VerificationIntention(Page):
    form_model = 'player'
    form_fields = ['verif_intent_1', 'verif_intent_2']

    @staticmethod
    def vars_for_template(player):
        return dict(
            progress=global_progress(13),
            scale_label="Please answer the following questions.",
            q1=dict(
                name='verif_intent_1',
                label="Would you like to look up additional information on this topic?",
                choices=[dict(value=1, text='yes'), dict(value=0, text='no')],
            ),
            q2_name='verif_intent_2',
            q2_choices=[dict(value=1, text='yes'), dict(value=0, text='no')],
        )


class Credibility(Page):
    form_model = 'player'
    form_fields = ['cred_accurate', 'cred_authentic', 'cred_believable']

    @staticmethod
    def vars_for_template(player):
        anchors = ["very poorly", "poorly", "somewhat poorly", "moderately",
                   "somewhat well", "well", "very well"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 8)]
        return dict(
            progress=global_progress(15),
            content_intro="Please rate the answers you received from the AI chatbot.",
            scale_label="How well do the following adjectives describe the AI chatbot's answers?",
            questions=[
                dict(name='cred_accurate', label="accurate", choices=choices),
                dict(name='cred_authentic', label="authentic", choices=choices),
                dict(name='cred_believable', label="believable", choices=choices),
            ],
        )


class PerceivedUncertainty(Page):
    form_model = 'player'
    form_fields = ['uncert_1', 'uncert_2', 'uncert_3']

    @staticmethod
    def vars_for_template(player):
        anchors = ["not at all uncertain", "slightly uncertain", "somewhat uncertain", "moderately uncertain",
                   "fairly uncertain", "very uncertain", "extremely uncertain"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 8)]
        return dict(
            progress=global_progress(16),
            content_intro="We would like to know how you feel after the information you just received.",
            scale_label="Please select an answer for each question below.",
            questions=[
                dict(name='uncert_1',
                     label="To what extent do you think the information you received about social media bans is certain or uncertain?",
                     choices=choices),
                dict(name='uncert_2',
                     label="How much uncertainty do you think there is about social media bans?",
                     choices=choices),
                dict(name='uncert_3',
                     label="After this search, how uncertain do you feel about this topic?",
                     choices=choices),
            ],
        )


class KnowledgeSufficiencyPost(Page):
    form_model = 'player'
    form_fields = ['know_post', 'suff_post']

    @staticmethod
    def vars_for_template(player):
        return dict(
            progress=global_progress(14),
            content_intro="After your search, please answer the following two questions.",
            fillin_instruction="Please answer the following two questions using the slider.",
            questions=[
                dict(name='know_post',
                     label="How much do you feel you know about social media bans for children and adolescents under 16?"),
                dict(name='suff_post',
                     label="How much would you need to know about this topic to feel sufficiently informed?"),
            ],
        )


class PerceivedCompleteness(Page):
    form_model = 'player'
    form_fields = ['complete_1', 'complete_2', 'complete_3']

    @staticmethod
    def vars_for_template(player):
        anchors = ["strongly disagree", "disagree", "somewhat disagree", "neither agree nor disagree",
                   "somewhat agree", "agree", "strongly agree"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 8)]
        return dict(
            progress=global_progress(17),
            content_intro="Please rate how complete the AI's answers felt to you.",
            scale_label="Please indicate how much you agree with each of the following statements.",
            questions=[
                dict(name='complete_1',
                     label="I am confident the AI's answers covered all the important aspects of social media bans.",
                     choices=choices),
                dict(name='complete_2',
                     label="The AI's responses gave me the complete picture on social media bans.",
                     choices=choices),
                dict(name='complete_3',
                     label="There are probably important aspects of social media bans the AI did not mention.",
                     choices=choices),
            ],
        )


class PostAttitude(Page):
    form_model = 'player'
    form_fields = ['attitude_post']

    @staticmethod
    def vars_for_template(player):
        anchors = ["strongly disagree", "disagree", "slightly disagree",
                   "slightly agree", "agree", "strongly agree"]
        return dict(
            progress=global_progress(18),
            content_intro="After your search, we would like to know your current view on the topic.",
            scale_label="Please indicate how much you agree with the following statement.",
            questions=[
                dict(name='attitude_post',
                     label="Banning social media for children and adolescents under the age of 16 is the right thing to do.",
                     choices=[dict(value=i, text=anchors[i - 1]) for i in range(1, 7)]),
            ],
        )


class SIHS(Page):
    form_model = 'player'
    form_fields = ['sihs_7', 'sihs_8', 'sihs_9']

    @staticmethod
    def vars_for_template(player):
        anchors = ["not at all like me", "a little like me", "somewhat like me", "mostly like me", "very much like me"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 6)]
        return dict(
            progress=global_progress(19),
            content_intro="The following statements are about your personal views on the topic you just searched.",
            scale_label="Please indicate how much each statement applies to you.",
            questions=[
                dict(name='sihs_7', label="My views about social media bans today may someday turn out to be wrong.",
                     choices=choices),
                dict(name='sihs_8', label="When it comes to my views about social media bans I may be overlooking evidence.",
                     choices=choices),
                dict(name='sihs_9', label="My views about social media bans may change with additional evidence or information.",
                     choices=choices),
            ],
        )


class GIHS_post(Page):
    form_model = 'player'
    form_fields = ['gihs_post_1', 'gihs_post_2', 'gihs_post_3', 'gihs_post_4', 'gihs_post_5', 'gihs_post_6']

    @staticmethod
    def vars_for_template(player):
        anchors = ["not at all like me", "a little like me", "somewhat like me", "mostly like me", "very much like me"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 6)]
        return dict(
            progress=global_progress(20),
            content_intro="We have a few questions about how you feel at this moment.",
            scale_label="Please indicate how much each statement applies to you.",
            questions=[
                dict(name='gihs_post_1',
                     label="I question my own opinions, positions, and viewpoints because they could be wrong.",
                     choices=choices),
                dict(name='gihs_post_2', label="I reconsider my opinions when presented with new evidence.",
                     choices=choices),
                dict(name='gihs_post_3', label="I recognize the value in opinions that are different from my own.",
                     choices=choices),
                dict(name='gihs_post_4', label="I accept that my beliefs and attitudes may be wrong.",
                     choices=choices),
                dict(name='gihs_post_5',
                     label="In the face of conflicting evidence, I am open to changing my opinions.",
                     choices=choices),
                dict(name='gihs_post_6',
                     label="I like finding out new information that differs from what I already think is true.",
                     choices=choices),
            ],
        )


class AIPerception(Page):
    form_model = 'player'
    form_fields = [
        'comp_1', 'comp_2', 'comp_3',
        'warm_1', 'warm_2', 'warm_3',
        'aih_1', 'aih_2', 'aih_3', 'aih_4', 'aih_5', 'aih_6',
    ]

    @staticmethod
    def vars_for_template(player):
        anchors = ["strongly disagree", "disagree", "neither agree nor disagree", "agree", "strongly agree"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 6)]
        return dict(
            progress=global_progress(21),
            content_intro="Please share your impressions of the AI chatbot you just interacted with.",
            scale_label="Please indicate how much you agree with the following statements.",
            groups=[
                dict(
                    header="",
                    stem="The AI chatbot was…",
                    questions=[
                        dict(name='comp_1', label="…knowledgeable.", choices=choices),
                        dict(name='comp_2', label="…competent.", choices=choices),
                        dict(name='comp_3', label="…capable.", choices=choices),
                        dict(name='warm_1', label="…warm.", choices=choices),
                        dict(name='warm_2', label="…friendly.", choices=choices),
                        dict(name='warm_3', label="…personal.", choices=choices),
                    ],
                ),
                dict(
                    header="",
                    stem="The AI chatbot…",
                    questions=[
                        dict(name='aih_1', label="…acknowledged uncertainty.", choices=choices),
                        dict(name='aih_2', label="…considered alternative viewpoints.", choices=choices),
                        dict(name='aih_3', label="…presented its answer as definitive.", choices=choices),
                        dict(name='aih_4', label="…recognized its own knowledge limitations.", choices=choices),
                        dict(name='aih_5', label="…admitted when it did not know something.", choices=choices),
                        dict(name='aih_6', label="…expressed the fallibility of knowledge.", choices=choices),
                    ],
                ),
            ],
        )


class Naturality(Page):
    form_model = 'player'
    form_fields = ['natural_similar', 'natural_feel', 'natural_open']

    @staticmethod
    def vars_for_template(player):
        similar_anchors = ["very different", "different", "somewhat different", "moderately similar",
                           "somewhat similar", "similar", "very similar"]
        natural_anchors = ["very unnatural", "unnatural", "somewhat unnatural", "moderately natural",
                           "somewhat natural", "natural", "very natural"]
        return dict(
            progress=global_progress(22),
            content_intro="A few last questions about your experience with the chat interface.",
            scale_label='',
            questions=[
                dict(name='natural_similar',
                     label="How similar was the interaction with this AI chatbot to AI chatbots you are familiar with (e.g., ChatGPT)?",
                     choices=[dict(value=i, text=similar_anchors[i - 1]) for i in range(1, 8)]),
                dict(name='natural_feel',
                     label="How natural did the interaction with the AI chatbot feel?",
                     choices=[dict(value=i, text=natural_anchors[i - 1]) for i in range(1, 8)]),
            ],
        )


page_sequence = [
    VerificationIntention,
    KnowledgeSufficiencyPost,
    Credibility,
    PerceivedUncertainty,
    PerceivedCompleteness,
    PostAttitude,
    SIHS,
    GIHS_post,
    AIPerception,
    Naturality,
]
