from otree.api import *
from study_progress import global_progress

doc = """
Debriefing page shown after the study is complete.
"""


class C(BaseConstants):
    NAME_IN_URL = 'outro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


########################################################
# Pages                                                #
########################################################

class Debriefing(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(progress=global_progress(23))


page_sequence = [
    Debriefing,
]
