FROM python:3.11.6-slim

ARG HOST_USER

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y docker.io gcc python3-dev libpq-dev musl-dev --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt


RUN useradd -m -d /home/$HOST_USER $HOST_USER

RUN chown -R $HOST_USER:$HOST_USER /code

USER $HOST_USER

COPY . /code/