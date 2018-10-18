FROM python:2

MAINTAINER omrigann@gmail.com

WORKDIR /app

COPY requirements_local.txt /app/requirements.txt
COPY anytask /app/anytask
COPY dependencies /app/dependencies
COPY configs/docker/production/settings.py /app/anytask/settings_local.py
COPY configs/uwsgi/


RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y gettext && \
    pip install -r requirements.txt && \
    pip install uwsgi && \
    python /app/anytask/manage.py collectstatic --noinput && \
    python /app/anytask/manage.py compilemessages && \
    python /app/setup.py install

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY docker/production-nginx/nginx-app.conf /etc/nginx/sites-available/default
COPY docker/production-nginx/supervisor-app.conf /etc/supervisor/conf.d/

COPY . /app
RUN python /app/anytask/manage.py collectstatic --noinput
RUN python /app/anytask/manage.py compilemessages
RUN python /app/setup.py install

EXPOSE 80
CMD ["supervisord", "-n"]
