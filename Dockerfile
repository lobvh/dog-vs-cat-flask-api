FROM python:3.7

RUN apt-get update && apt-get install -y python3 python3-pip sudo

RUN useradd -m goceovoono

WORKDIR /Users/goceovoono/Desktop/app

COPY --chown=goceovoono . /Users/goceovoono/Desktop/app/

RUN chown -R goceovoono:goceovoono /Users/goceovoono/Desktop/

USER goceovoono

RUN pip3 install --upgrade pip

RUN cd /Users/goceovoono/Desktop/app/ && pip3 install -r requirements.txt
