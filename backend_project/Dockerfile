FROM python:3.13.2-slim

WORKDIR /backend/cleanly_backend

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

COPY ./backend/cleanly_backend/requirements.txt ./
RUN pip install -r requirements.txt