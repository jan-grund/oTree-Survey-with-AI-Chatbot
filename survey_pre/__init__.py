from otree.api import *
from study_progress import global_progress

doc = """
Survey administered before the chat interaction.
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey_pre'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # ── Demographics ───────────────────────────────────
    age = models.IntegerField(
        label="How old are you?", min=16, max=120, error_message="Please enter a valid age between 16 and 120.")
    gender = models.StringField(
        label="Which gender do you identify with?",
        choices=["Male", "Female", "Different"],
        widget=widgets.RadioSelect)
    education = models.StringField(
        label="What is your highest level of education?",
        choices=[
            "I don't have a degree.",
            "Junior High School Diploma",
            "Middle School Diploma",
            "High School Diploma",
            "Bachelor's Degree",
            "Master's Degree",
            "Doctorate",
        ],
        widget=widgets.RadioSelect)
    occupation = models.StringField(
        label="What is your occupation?",
        choices=[
            "High school student",
            "College student",
            "Apprentice",
            "Employee",
            "Civil servant",
            "Self-employed",
            "Unemployed/job seeker",
            "Retiree",
            "Other",
        ],
        widget=widgets.RadioSelect)

    # ── Experience with AI Chatbots ─────────────────────
    # 1 = never, 7 = several times a day
    exp_1 = models.IntegerField(
        label="How frequently do you use AI chatbots in general?",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    exp_2 = models.IntegerField(
        label="How frequently do you use AI-powered answers from traditional search engines (e.g., Google's AI Overview, Bing Copilot)?",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    exp_3 = models.IntegerField(
        label="How frequently do you explicitly use AI chatbots to search up information",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)

    # ── General Trust in AI ─────────────────────────────
    # 1 = strongly disagree, 5 = strongly agree
    trust_1 = models.IntegerField(
        label="I believe in AI chatbots when searching for information.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    trust_2 = models.IntegerField(
        label="I trust AI chatbots when searching for information.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    trust_3 = models.IntegerField(
        label="I distrust AI chatbots when searching for information.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    trust_4 = models.IntegerField(
        label="AI chatbots are designed to be trustworthy.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    trust_5 = models.IntegerField(
        label="I can depend on AI when searching for information.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # ── General Verification Behavior ───────────────────
    # 1 = strongly disagree, 7 = strongly agree
    verif_beh_1 = models.IntegerField(
        label="When looking up information I always use other sources than AI-powered answers.",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    verif_beh_2 = models.IntegerField(
        label="When using AI to look up information I always visit external sources to verify the given information.",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)

    # ── Intellectual Humility (GIHS) ─────────────────────
    # 1 = not at all like me, 5 = very much like me
    gihs_1 = models.IntegerField(
        label="I question my own opinions, positions, and viewpoints because they could be wrong.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    gihs_2 = models.IntegerField(
        label="I reconsider my opinions when presented with new evidence.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    gihs_3 = models.IntegerField(
        label="I recognize the value in opinions that are different from my own.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    gihs_4 = models.IntegerField(
        label="I accept that my beliefs and attitudes may be wrong.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    gihs_5 = models.IntegerField(
        label="In the face of conflicting evidence, I am open to changing my opinions.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    gihs_6 = models.IntegerField(
        label="I like finding out new information that differs from what I already think is true.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # ── Specific Intellectual Humility Scale (SIHS), pre-interaction ──
    # 1 = not at all like me, 5 = very much like me
    sihs_pre_7 = models.IntegerField(
        label="My views about social media bans today may someday turn out to be wrong.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    sihs_pre_8 = models.IntegerField(
        label="When it comes to my views about social media bans I may be overlooking evidence.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    sihs_pre_9 = models.IntegerField(
        label="My views about social media bans may change with additional evidence or information.",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # ── Subjective Prior Knowledge and Sufficiency ──────
    # 0 = knowing nothing, 100 = knowing everything you could possibly know
    know_pre = models.IntegerField(
        label="How much do you feel you know about social media bans for children and adolescents under 16?",
        min=0, max=100)
    suff_pre = models.IntegerField(
        label="How much would you need to know about this topic to feel sufficiently informed?",
        min=0, max=100)

    # ── Prior Attitude ───────────────────────────────────
    attitude = models.IntegerField(
        label="Banning social media for children and adolescents under the age of 16 is the right thing to do.",
        choices=[1, 2, 3, 4, 5, 6], widget=widgets.RadioSelectHorizontal)
    att_certainty = models.IntegerField(
        label="How certain are you of your opinion on this topic?",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    att_importance = models.IntegerField(
        label="How important is this topic to you personally?",
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)


########################################################
# Pages                                                #
########################################################

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'occupation']

    @staticmethod
    def vars_for_template(player):
        return dict(progress=global_progress(3))


class Experience(Page):
    form_model = 'player'
    form_fields = ['exp_1', 'exp_2', 'exp_3']

    @staticmethod
    def vars_for_template(player):
        anchors = ["never", "rarely", "occasionally", "sometimes", "often", "very often", "several times a day"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 8)]
        return dict(
            progress=global_progress(4),
            content_intro="To start, we have a few questions about how you use technology in your everyday life.",
            scale_label="Please indicate how frequently the following applies to you.",
           questions=[
                dict(name='exp_1', label="How frequently do you use AI chatbots?",
                    choices=choices),
                dict(name='exp_2', label="How frequently do you use AI-powered answers from traditional search engines (e.g., Google's AI Overview, Bing Copilot)?",
                    choices=choices),
                dict(name='exp_3', label="How frequently do you use AI chatbots specifically to search for information on a topic?",
                    choices=choices),
            ],
        )


class Trust(Page):
    form_model = 'player'
    form_fields = ['trust_1', 'trust_2', 'trust_3', 'trust_4', 'trust_5']

    @staticmethod
    def vars_for_template(player):
        anchors = ["strongly disagree", "disagree", "neither agree nor disagree", "agree", "strongly agree"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 6)]
        return dict(
            progress=global_progress(5),
            content_intro="The next questions are about your general views on AI tools.",
            scale_label="Please indicate how much you agree with each of the following statements.",
            questions=[
                dict(name='trust_1', label="I believe in AI chatbots when searching for information.",
                    choices=choices),
                dict(name='trust_2', label="I trust AI chatbots when searching for information.",
                    choices=choices),
                dict(name='trust_3', label="I distrust AI chatbots when searching for information.",
                    choices=choices),
                dict(name='trust_4', label="AI chatbots are designed to be trustworthy.",
                    choices=choices),
                dict(name='trust_5', label="I can depend on AI chatbots when searching for information.",
                    choices=choices),
            ],
        )


class VerificationBehavior(Page):
    form_model = 'player'
    form_fields = ['verif_beh_1', 'verif_beh_2']

    @staticmethod
    def vars_for_template(player):
        anchors = ["strongly disagree", "disagree", "somewhat disagree", "neither agree nor disagree",
                   "somewhat agree", "agree", "strongly agree"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 8)]
        return dict(
            progress=global_progress(6),
            content_intro="The following questions are about your everyday information habits.",
            scale_label="Please indicate how much you agree with each of the following statements.",
            questions=[
                dict(name='verif_beh_1',
                     label="When looking up information I always use other sources than AI answers.",
                     choices=choices),
                dict(name='verif_beh_2',
                     label="When using AI to look up information I always visit external sources to verify the given information.",
                     choices=choices),
            ],
        )


class GIHS(Page):
    form_model = 'player'
    form_fields = ['gihs_1', 'gihs_2', 'gihs_3', 'gihs_4', 'gihs_5', 'gihs_6']

    @staticmethod
    def vars_for_template(player):
        anchors = ["not at all like me", "a little like me", "somewhat like me", "mostly like me", "very much like me"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 6)]
        return dict(
            progress=global_progress(7),
            content_intro="The following statements describe different ways people think about their own views and beliefs.",
            scale_label="Please indicate how much each statement applies to you.",
            questions=[
                dict(name='gihs_1',
                     label="I question my own opinions, positions, and viewpoints because they could be wrong.",
                     choices=choices),
                dict(name='gihs_2', label="I reconsider my opinions when presented with new evidence.",
                     choices=choices),
                dict(name='gihs_3', label="I recognize the value in opinions that are different from my own.",
                     choices=choices),
                dict(name='gihs_4', label="I accept that my beliefs and attitudes may be wrong.",
                     choices=choices),
                dict(name='gihs_5',
                     label="In the face of conflicting evidence, I am open to changing my opinions.",
                     choices=choices),
                dict(name='gihs_6',
                     label="I like finding out new information that differs from what I already think is true.",
                     choices=choices),
            ],
        )


class SIHS_pre(Page):
    form_model = 'player'
    form_fields = ['sihs_pre_7', 'sihs_pre_8', 'sihs_pre_9']

    @staticmethod
    def vars_for_template(player):
        anchors = ["not at all like me", "a little like me", "somewhat like me", "mostly like me", "very much like me"]
        choices = [dict(value=i, text=anchors[i - 1]) for i in range(1, 6)]
        return dict(
            progress=global_progress(8),
            content_intro="The following statements are about your personal views on social media bans.",
            scale_label="Please indicate how much each statement applies to you.",
            questions=[
                dict(name='sihs_pre_7', label="My views about social media bans today may someday turn out to be wrong.",
                     choices=choices),
                dict(name='sihs_pre_8', label="When it comes to my views about social media bans I may be overlooking evidence.",
                     choices=choices),
                dict(name='sihs_pre_9', label="My views about social media bans may change with additional evidence or information.",
                     choices=choices),
            ],
        )


class KnowledgeSufficiency(Page):
    form_model = 'player'
    form_fields = ['know_pre', 'suff_pre']

    @staticmethod
    def vars_for_template(player):
        return dict(
            progress=global_progress(9),
            content_intro="We have two quick questions about social media bans for children and adolescents under 16.",
            fillin_instruction="Please answer the following two questions using the slider.",
            questions=[
                dict(name='know_pre',
                     label="How much do you feel you know about social media bans for children and adolescents under 16?"),
                dict(name='suff_pre',
                     label="How much would you need to know about this topic to feel sufficiently informed?"),
            ],
        )


class PriorAttitude(Page):
    form_model = 'player'
    form_fields = ['attitude', 'att_certainty', 'att_importance']

    @staticmethod
    def vars_for_template(player):
        attitude_anchors = ["strongly disagree", "disagree", "slightly disagree",
                            "slightly agree", "agree", "strongly agree"]
        certainty_anchors = ["not at all certain", "slightly certain", "somewhat certain", "moderately certain",
                             "fairly certain", "very certain", "completely certain"]
        importance_anchors = ["not at all important", "slightly important", "somewhat important",
                              "moderately important", "fairly important", "very important", "extremely important"]
        return dict(
            progress=global_progress(10),
            content_intro="In the following, we focus on a current topic of debate: whether social media should be banned for children and adolescents under the age of 16. We would first like to know your opinion on this question.",
            scale_label="Please indicate how much you agree with the following statement, and how you feel about the topic.",
            questions=[
                dict(name='attitude', label="Banning social media for children and adolescents under the age of 16 is the right thing to do.",
                     choices=[dict(value=i, text=attitude_anchors[i - 1]) for i in range(1, 7)]),
                dict(name='att_certainty', label="How certain are you of your opinion on this topic?",
                     choices=[dict(value=i, text=certainty_anchors[i - 1]) for i in range(1, 8)]),
                dict(name='att_importance', label="How important is this topic to you personally?",
                     choices=[dict(value=i, text=importance_anchors[i - 1]) for i in range(1, 8)]),
            ],
        )


class InteractionInstruction(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(progress=global_progress(11))


page_sequence = [
    Demographics,
    Experience,
    Trust,
    VerificationBehavior,
    GIHS,
    SIHS_pre,
    KnowledgeSufficiency,
    PriorAttitude,
    InteractionInstruction,
]
