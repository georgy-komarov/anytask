FROM python:2

WORKDIR /app

COPY requirements_local.txt /app/requirements.txt
COPY anytask /app/anytask
COPY dependencies /app/dependencies
COPY configs/docker/production/entrypoint.py /app/entrypoint.py
COPY configs/docker/production/settings.py /app/anytask/settings_production.py

RUN apt-get update && apt-get upgrade -y && apt-get install -y gettext
RUN pip install -r requirements.txt && pip install uwsgi psycopg2
RUN python /app/anytask/manage.py compilemessages

ENTRYPOINT echo 'exec(open("/app/entrypoint.py").read())' | python /app/anytask/manage.py shell && uwsgi --socket :8000 --module anytask.wsgi
