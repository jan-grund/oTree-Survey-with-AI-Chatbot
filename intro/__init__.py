from otree.api import *
from study_progress import global_progress

doc = """
Welcome and consent pages shown before the rest of the study.
"""


class C(BaseConstants):
    NAME_IN_URL = 'intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(initial=False, widget=widgets.CheckboxInput)


########################################################
# Pages                                                #
########################################################

class Welcome(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(progress=global_progress(1))

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Prolific passes PROLIFIC_PID/STUDY_ID/SESSION_ID via the start URL, but oTree's
        # entry redirects (join/room -> InitializeParticipant -> first page) strip all query
        # params except participant_label, which IS persisted server-side. So the study's
        # start link must encode all three as participant_label=PID~STUDY~SESSION.
        participant = player.participant
        label = participant.label or ''
        parts = label.split('~')
        participant.prolific_pid = parts[0] if len(parts) > 0 else ''
        participant.study_id = parts[1] if len(parts) > 1 else ''
        participant.prolific_session_id = parts[2] if len(parts) > 2 else ''


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def vars_for_template(player):
        return dict(progress=global_progress(2))

    @staticmethod
    def error_message(player, values):
        if not values.get('consent'):
            return 'Please tick the box to confirm your consent before continuing.'


page_sequence = [
    Welcome,
    Consent,
]
