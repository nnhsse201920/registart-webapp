FROM python:3.6-alpine

RUN adduser -D registart-webapp
WORKDIR /registart-webapp

COPY requirements.txt requirements.txt
RUN python -m venv env
RUN env/bin/pip install -r requirements.txt
RUN env/bin/pip install gunicorn 

COPY survey.py .env config.py boot.sh ./ 
COPY app app
COPY migrations migrations
RUN chmod a+x boot.sh

ENV FLASK_APP survey.py

RUN chown -R registart-webapp:registart-webapp ./
RUN apk add gcc
RUN apk add --no-cache libressl-dev musl-dev libffi-dev
RUN env/bin/pip install --no-cache-dir cryptography
USER registart-webapp

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
