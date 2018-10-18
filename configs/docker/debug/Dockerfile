FROM python:2

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY anytask /app/anytask
COPY dependencies /app/dependencies
COPY configs/docker/debug/settings.py /app/anytask/settings_local.py

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y gettext && \
    pip install -r requirements.txt && \
    python /app/anytask/manage.py compilemessages

CMD python /app/anytask/manage.py syncdb --migrate --noinput && \
    python /app/anytask/manage.py runserver 0.0.0.0:8000 -v 3 --traceback
