FROM python:3.11.5-slim

# Set variables
ARG BOT_TOKEN

WORKDIR /root/bot

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .
RUN echo "BOT_TOKEN='${BOT_TOKEN}'" > config.py

ENTRYPOINT ["python", "main.py"]