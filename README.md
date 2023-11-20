
# Acunetix API + Aiogram 3 + Docker = AcuBot ❤️

## Config & Install & Run

#### Installation:
```bash
# Install docker
apt -y update && apt -y install curl sudo git
curl -fsSL https://get.docker.com -o install-docker.sh
sudo sh install-docker.sh

# Download and configure project
git clone https://github.com/fuad00/acubot && cd acubot
echo 'BOT_TOKEN=579013110:AAGS6inF_Paste_Your_Bot_Token
POSTGRES_DB=acubot
POSTGRES_PASSWD=ChangeMeLater' > .env

# Build and run project
docker compose build
docker compose up -d # remove '-d' for seeing logs in realtime
```


## Support
<details>
    <summary>btc</summary>
	<code>bc1q90ma5sgmh39fkl29xahdh822tnf4hexxfsqguq</code>
</details>