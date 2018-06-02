import os

# Required for Django 1.5
# Set server domain(s)
ALLOWED_HOSTS = ['domain.com', 'yourdoamin.ru']

# Set E-MAIL Settings
# Use EMAIL_USE_SSL and EMAIL_USE_TLS vars for SSL support
EMAIL_BACKEND = 'mail_smtp_ssl.EmailBackend'

# SMTP Server host
EMAIL_HOST = 'smtp.mailserverexample.ru'

# SMTP Server port
EMAIL_PORT = 465

# Sender SMTP username
EMAIL_HOST_USER = 'mail_login_here'

# Sender SMTP password
EMAIL_HOST_PASSWORD = 'mail_passwd_here'

# Connection settings
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

# Or use mailgun
# EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
# MAILGUN_ACCESS_KEY = 'API-KEY'
# MAILGUN_SERVER_NAME = 'DOMAIN.COM'

# Set FROM field
DEFAULT_FROM_EMAIL = 'example@mail.ru'

# Set admin for e-mail error notifications
ADMINS = (('Admin Adminov', 'exampleadmin@mail.ru'), ('Name Lastname', 'exampleadmin2@mail.ru'))

# DO NOT DELETE THIS LINE!
MANAGERS = ADMINS

# Set paths + locale fix
# DO NOT CHANGE THESE LINES!
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
LOCALE_PATHS = (os.path.join(PROJECT_PATH, 'locale'),)  # LOCALE_PATHS must be tuple

# Set secret key
# Make this unique, and don't share it with anybody.
# manage.py generate_secret_key
SECRET_KEY = 'SUPER_SECRET_KEY'

# ReCaptcha support
# FIXME Not working
RECAPTCHA_PUBLIC_KEY = "RECAPTCHA_PUBLIC_KEY"
RECAPTCHA_PRIVATE_KEY = "RECAPTCHA_PRIVATE_KEY"

# Setup ReviewBoard
# FIXME Not working
RB_API_URL = "http://localhost:8080"
RB_API_USERNAME = "anytask"
RB_API_PASSWORD = "P@ssw0rd"
RB_API_DEFAULT_REVIEW_GROUP = 'teachers'
RB_SYMLINK_DIR = '/var/lib/anytask/repos/'

# Set contest integration
CONTEST_OAUTH = 'ADMIN_TOKEN_HERE'
CONTEST_OAUTH_ID = 'APP_ID_FROM_OAUTH.YANDEX.RU'
CONTEST_OAUTH_PASSWORD = 'APP_PASSWD_FROM_OAUTH.YANDEX.RU'

# Set specific compilers for courses
# TODO Understand how it works
CONTEST_EXTENSIONS_COURSE = {
    30: {
        ".py": "python3"
    },
    13: {
        ".h": "make2"
    },
    61: {
        ".h": "make2"
    }
}

# Setup Yandex.Passport integration
PASSPORT_OAUTH_ID = 'APP_ID_FROM_OAUTH.YANDEX.RU'
PASSPORT_OAUTH_PASSWORD = 'APP_PASSWD_FROM_OAUTH.YANDEX.RU'

# File uploader settings
MAX_FILE_SIZE = 1024 * 1024  # 1 Mb
MAX_FILES_NUMBER = 10
ACCEPTED_FILE_TYPES = '\.+(jpg|jpeg|png|gif|bmp|sh|bas|pas|cpp|c|cs|java|php|py|txt|rtf|doc|docx|xls|xlsx|ppt|pptx)$'

ACCOUNT_ACTIVATION_DAYS = 7
INVITE_EXPIRED_DAYS = 180

# If everything works, disable debug
# DEBUG = False

# Close registration after year start if needed
# REGISTRATION_OPEN = False

# RENAME THIS FILE TO settings_local.py !!!

# Do manage.py makemessages -l ru
# and manage.py compilemessages -l ru
# to generate translations
