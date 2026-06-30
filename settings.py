from os import environ
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


SESSION_CONFIGS = [
    dict(
        name='humble_ai_study',
        app_sequence=['intro', 'survey_pre', 'chat_simple', 'survey_post', 'outro'],
        num_demo_participants=1,
    ),
]
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['condition', 'prolific_pid', 'study_id', 'prolific_session_id']
SESSION_FIELDS = []


# rooms
ROOMS = [
    dict(
        name='studyRoom1',
        display_name='Study Room 1',
    ),
    # dict(
    #     name='chat_japanese_room',
    #     display_name='Chat Japanese Room',
    #     participant_label_file='_rooms/chat_japanese_room.txt',
    #     use_secure_urls=False,  # セキュアURLを無効化してリンクを繰り返し使用可能に
    # ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '6929828123368'
