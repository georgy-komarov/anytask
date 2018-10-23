FROM python:2

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y gettext && \
    pip install -r requirements.txt

COPY configs/docker/debug/entrypoint.py /app/entrypoint.py

ENTRYPOINT cd anytask && \
           echo 'execfile("/app/entrypoint.py")' | python manage.py shell && \
           python manage.py runserver 0.0.0.0:8000 -v 3 --traceback
