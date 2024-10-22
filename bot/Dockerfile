FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade -r /app/requirements.txt 
# --no-cache-dir if you want to upgrade modules

# Copy project
COPY . .

ENTRYPOINT ["python", "main.py"]