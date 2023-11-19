
# Acunetix API + Aiogram 3 + Docker Compose = AcuBot ❤️

## config/install/run

1. Install docker:
```bash
apt -y update && apt -y install curl sudo git
curl -fsSL https://get.docker.com -o install-docker.sh
sudo sh install-docker.sh
```

2. Download and configure project:
```bash
git clone https://github.com/fuad00/acubot && cd acubot
echo "bot_token = '<YOUR_TGBOT_TOKEN>'" > bot/config.py # TODO: change to .env
```

3. Build and run project:
```bash
docker compose build
docker compose up -d # remove -d for logging (also if already running)
```

## Support
<details>
    <summary>btc</summary>
	<code>bc1q90ma5sgmh39fkl29xahdh822tnf4hexxfsqguq</code>
</details>