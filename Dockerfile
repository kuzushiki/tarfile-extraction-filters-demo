FROM python:3.11.4-slim-bookworm

RUN pip install --upgrade pip
RUN pip install -U flask

WORKDIR /usr/src/app
COPY ./src .
