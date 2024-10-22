FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
# ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install requirements
COPY ./requirements.txt /app/requirements.txt
RUN uv pip install -r requirements.txt --system 
# --no-cache-dir if you want to upgrade modules

# Copy project
COPY . .

ENTRYPOINT ["python", "main.py"]