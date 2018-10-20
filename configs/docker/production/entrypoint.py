from __future__ import print_function

import os
import subprocess


class StartHelper:
    def __init__(self):
        self.STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
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

    def first_migrations(self):
        apps_order = ['years',
                      'groups',
                      'courses',
                      'tasks',
                      'issues',
                      'mail']

        self.migrate()
        for app in apps_order:
            print(subprocess.check_output('python manage.py {}'.format(app), shell=True))
        self.migrate()

    def migrate(self):
        cmd = 'python manage.py syncdb --migrate --noinput'
        print(subprocess.check_output(cmd, shell=True))


PROJECT_PATH = '/app/anytask/'

if __name__ == '__main__':
    os.chdir(PROJECT_PATH)

    sh = StartHelper()
    first_run = sh.is_first_run()

    # Collect static if needed
    if not sh.has_static():
        sh.collect_static()

    # Migration on first startup
    if first_run:
        sh.first_migrations()

    if os.environ.get('AUTO_MIGRATE') == 'True':
        sh.migrate()

    print('Pre-start check completed!')
