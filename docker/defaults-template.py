import os


class DefaultConfig(object):
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    CSRF_ENABLED = True
    # secret key for flask sessions http://flask.pocoo.org/docs/1.0/quickstart/#sessions
    SECRET_KEY = open('/var/run/secrets/SECRET_KEY', 'r').read().strip() if os.path.exists('/var/run/secrets/SECRET_KEY_PASS') else '<3 Please CHANGE THIS KEY ! <3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWITTER_CONSUMER_KEY = '<your_consumer_key>'
    # TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_PASS','')
    TWITTER_CONSUMER_SECRET = open('/var/run/secrets/TWITTER_PASS', 'r').read().strip() if os.path.exists('/var/run/secrets/TWITTER_PASS') else ''
    INSTAGRAM_CLIENT_ID = '<your_instagram_client_id>'
    INSTAGRAM_SECRET = open('/var/run/secrets/INSTAGRAM_PASS', 'r').read().strip() if os.path.exists('/var/run/secrets/INSTAGRAM_PASS') else ''
    # define in config.py
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://moa:moa@localhost/moa'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/moa.db'
    SEND = True
    SENTRY_DSN = ''
    HEALTHCHECKS = []
    MAIL_SERVER = None
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '<your_email_user_name>'
    MAIL_PASSWORD = open('/var/run/secrets/SMTP_PASS', 'r').read().strip() if os.path.exists('/var/run/secrets/SMTP_PASS') else ''
    MAIL_TO = '<your_default_notification_email>'
    MAIL_DEFAULT_SENDER = '<your_default_sender_override>'
    TWITTER_BLACKLIST = []
    MASTODON_BLACKLIST = []
    WORKER_JOBS = 1
    MAX_MESSAGES_PER_RUN = 5

    # This option prevents Twitter replies and mentions from occuring when a toot contains @user@twitter.com. This
    # behavior is against Twitter's rules.
    SANITIZE_TWITTER_HANDLES = True

    SEND_DEFERRED_EMAIL = False
    SEND_DEFER_FAILED_EMAIL = False
    MAINTENANCE_MODE = False

    STATS_POSTER_BASE_URL = None
    STATS_POSTER_ACCESS_TOKEN = None

    TRUST_PROXY_HEADERS = False
