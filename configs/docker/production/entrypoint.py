from __future__ import print_function

import os
import subprocess

STATIC_PATH = '/app/anytask/static'
if not (os.path.exists(STATIC_PATH) and os.listdir(STATIC_PATH)):
    print('Static files not found! Collecting...')
    print(subprocess.check_output('python /app/anytask/manage.py collectstatic --noinput', shell=True))

print('Pre-start check completed!')
