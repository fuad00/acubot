
# Acunetix API + Aiogram 3 + Docker = AcuBot ❤️

## Config & Install & Run

#### Installation:
```bash
# Install docker
apt -y update && apt -y install curl sudo git nano
curl -fsSL https://get.docker.com -o install-docker.sh
sudo sh install-docker.sh

# Download and configure project
git clone https://github.com/fuad00/acubot && cd acubot
cp .env.example .env
nano .env # Edit for production

# Build and run project
docker compose up --build -d
# remove '-d' for seeing logs in realtime
```


## Support
<details>
    <summary>btc</summary>
	<code>bc1qy0utklyuffvkz25sfx5vtydy4e0pgagmvajalc</code>
</details>


## Todo

1. push generated acunetix api key to psql database
2. add some bot basics and logic