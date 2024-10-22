
# Docker(Acunetix + Aiogram + FastAPI) = AcuBot ❤️

## Config & Install & Run

#### ⚒️ Installation:
```bash
# Install docker
apt -y update && apt -y install curl sudo git nano
curl -sSL https://get.docker.com/ | sh

# Download and configure project
git clone https://github.com/fuad00/acubot && cd acubot
cp .env.example .env
nano .env # Edit for production

# Build and run project
docker compose up --build -d
# remove '-d' for seeing logs in realtime
```


## 💰 Donations
<details>
    <summary>btc</summary>
	<code>bc1qy0utklyuffvkz25sfx5vtydy4e0pgagmvajalc</code>
</details>


## ✍️ TODO

1. add some bot basics and logic
2. Start developing fastapi