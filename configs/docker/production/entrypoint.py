from __future__ import print_function

import os
import subprocess


class StartHelper:
    def __init__(self):
        self.STATIC_PATH = '/app/anytask/static'
        self.STARTHELPER_FILE = '/app/.starthelper'  # This file is needed to check if app runs for the first time

    def is_first_run(self):
        flag = not os.path.exists(self.STARTHELPER_FILE)
        if not flag:
            open(self.STARTHELPER_FILE, 'w')
        return flag

    def has_static(self):
        return os.path.exists(self.STATIC_PATH) and os.listdir(self.STATIC_PATH)

    @staticmethod
    def collect_static():
        print(subprocess.check_output('python /app/anytask/manage.py collectstatic --noinput', shell=True))

    @staticmethod
    def first_migrations():
        commands = ['python manage.py syncdb --migrate --noinput --settings=settings_production',
                    'python manage.py migrate years --settings=settings_production',
                    'python manage.py migrate groups --settings=settings_production',
                    'python manage.py migrate courses --settings=settings_production',
                    'python manage.py migrate tasks --settings=settings_production',
                    'python manage.py migrate issues --settings=settings_production',
                    'python manage.py migrate mail --settings=settings_production',
                    'python manage.py syncdb --migrate --noinput --settings=settings_production']
        for cmd in commands:
            print(subprocess.check_output(cmd, shell=True))


sh = StartHelper()
first_run = sh.is_first_run()

# Collect static if needed
if not sh.has_static():
    sh.collect_static()

# Migration on first startup
if first_run:
    sh.first_migrations()

print('Pre-start check completed!')
