FROM python:2

WORKDIR /app

COPY requirements_local.txt /app/requirements.txt
COPY anytask /app/anytask
COPY dependencies /app/dependencies
COPY configs /app/configs
COPY configs/docker/production/settings.py /app/anytask/settings_local.py

RUN ls -la /app/configs/uwsgi

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y gettext

RUN pip install -r requirements.txt && \
    pip install uwsgi psycopg2

RUN python /app/anytask/manage.py collectstatic --noinput && \
    python /app/anytask/manage.py compilemessages

CMD ls -la /app/configs/uwsgi
