FROM python:3.7-alpine
MAINTAINER Dexture

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "$PYTHONPATH:/app"

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D runnerUser
USER runnerUser
