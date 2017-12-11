FROM jfloff/alpine-python:latest

ENV APP_ROOT /party-calculator-server/

WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}

RUN pip install pipenv

RUN pipenv install