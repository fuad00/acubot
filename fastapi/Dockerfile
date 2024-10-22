# Dockerfile

# pull the official docker image
FROM python:3.11.5

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .