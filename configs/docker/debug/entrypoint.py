import os
import subprocess
from django.conf import settings
from django.contrib.auth.models import User

BASE_DIR = settings.BASE_DIR
STATIC_PATH = settings.STATIC_ROOT
INIT_FILE = '/app/.init'  # This file is needed to check if app is running for the first time

MIGRATE_CMD = 'python manage.py syncdb --migrate --noinput'
CREATE_SUPERUSER_CMD = 'python manage.py createsuperuser --username={} --email={} --noinput'
COMPILE_MESSAGES_CMD = 'python manage.py compilemessages'
CREATE_SHAD_CMD = 'python manage.py create_shad < ./students.xml'
CLEAN_PYC_CMD = 'python manage.py clean_pyc'

os.chdir(BASE_DIR)

# Check if container is running for the first time
first_run = not os.path.exists(INIT_FILE)
if first_run:
    open(INIT_FILE, 'w')

# Migrate
subprocess.check_call(MIGRATE_CMD, shell=True)

# Compile .po translation files
subprocess.check_call(COMPILE_MESSAGES_CMD, shell=True)

# Clean *.pyc files
subprocess.check_call(CLEAN_PYC_CMD, shell=True)

# Create users 'anytask' and 'anytask.monitoring' if don't exist in DB
email = getattr('settings', 'EMAIL_HOST_USER', 'anytask@example.com')

for username in ['anytask', 'anytask.monitoring']:
    if not User.objects.filter(username=username).exists():
        subprocess.check_call(CREATE_SUPERUSER_CMD.format(username, email), shell=True)

        user = User.objects.get(username=username)
        user.set_password(username)
        user.save()

# Fill database with test students
if first_run and os.environ.get('FILL_DATABASE') == 'true':
    subprocess.check_call(CREATE_SHAD_CMD, shell=True)

print 'Pre-start check completed!'
