#!/bin/sh
cd /home/user/anytask/anytask && . ../.env/bin/activate && python manage.py fix_seminar_status --fix-all
exit 0
