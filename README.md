# AcuBot

Telegram-бот для управления сканированиями **Acunetix** (Dorker): запуск задач, статусы и отчёт об уязвимостях прямо в чат, плюс FastAPI-прослойка к API Acunetix.

## Архитектура

- `acunetix/` — клиент обёртки над API Acunetix Dorker
- `bot/` — Telegram-бот на aiogram
- `fastapi/` — REST-прослойка между ботом и Acunetix
- `init.sql` — инициализация БД

## Установка и запуск

```bash
# Install docker
apt -y update && apt -y install curl sudo git nano
curl -sSL https://get.docker.com/ | sh

# Download and configure project
git clone https://github.com/fuad00/acubot && cd acubot
cp .env.example .env
nano .env # BOT_TOKEN, ACUNETIX_HOST, ACUNETIX_API_KEY, ...

# Build and run project
docker compose up --build -d
# remove '-d' for seeing logs in realtime
```

## ⚠️ Дисклеймер

Только для авторизованного тестирования на собственном инсталлированном Acunetix. Использование против чужих инсталляций без разрешения — незаконно.

## 💰 Donations
<details>
    <summary>btc</summary>
    <code>bc1qy0utklyuffvkz25sfx5vtydy4e0pgagmvajalc</code>
</details>
