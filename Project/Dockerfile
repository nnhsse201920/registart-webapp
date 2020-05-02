FROM python:3.6-alpine

RUN adduser -D registart-webapp
WORKDIR /registart-webapp

COPY requirements.txt requirements.txt
RUN python -m venv env
RUN env/bin/pip install -r requirements.txt
RUN env/bin/pip install gunicorn 
RUN env/bin/pip install pymysql

COPY app.py .env config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP app.py

RUN chown -R registart-webapp:registart-webapp ./
USER registart-webapp

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
