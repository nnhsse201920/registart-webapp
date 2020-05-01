FROM python:3.6-alpine

RUN adduser -D registart-webapp
WORKDIR /home/registart-webapp

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app.py .env config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app.py

RUN chown -R registart-webapp:registart-webapp ./
RUN apk add gcc
RUN apk add --no-cache libressl-dev musl-dev libffi-dev
RUN venv/bin/pip install --no-cache-dir cryptography
USER registart-webapp

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
