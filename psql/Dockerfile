FROM ubuntu:22.04

# Set variables 
ARG DEBIAN_FRONTEND=noninteractive
ARG POSTGRES_DB
ARG POSTGRES_PASSWD

# Install requirements
RUN apt-get update && apt-get install -y \
    postgresql postgresql-contrib sudo

# Copy project
COPY . /root/psql
WORKDIR /root/psql

# Change working user
USER postgres

# Init database and set passwd
RUN service postgresql start &&\
    createdb "${POSTGRES_DB}" &&\
    psql -c "alter user postgres with password '${POSTGRES_PASSWD}';" &&\
    psql hashdog < 'init.sql'

# Change working user
USER root

# Allow connections from outside
RUN echo "listen_addresses = '*'" >> /etc/postgresql/$(ls /etc/postgresql/)/main/postgresql.conf
RUN echo "host    all        all     172.72.72.0/16       md5" >> /etc/postgresql/$(ls /etc/postgresql/)/main/pg_hba.conf
RUN sed -i 's/Etc\/UTC/Europe\/Moscow/' /etc/postgresql/$(ls /etc/postgresql/)/main/postgresql.conf


ENTRYPOINT ["/bin/bash", "-c", "service postgresql start"]