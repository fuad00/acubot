# Dockerfile

# pull the official docker image
FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# set work directory
WORKDIR /app

# set env variables
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install requirements
COPY requirements.txt .
RUN uv pip install -r requirements.txt --system 

# copy project
COPY . .
