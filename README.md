
# Acunetix API + Telegram Bot API = AcuBot

### AcuBot - это телеграм бот для мониторинга критических уязвимостей, найденных в вашем Acunetix

#### Написан на python 3


## Основные составляющие

- **bot.py** - 
 Тело программы.

- **requirements.txt**
  Зависимости.

 ## Установка
1. Устанавливаем сам питон:

		sudo apt-get update && apt-get -y install python3 python3-pip git

2. Клонируем репозиторий и устанавливаем необходимые модули:
	
	    git clone https://github.com/fuad00/acubot && cd acubot && pip3 install -r requirements.txt
	
3. Редактируем переменные строки в `bot.py` на строках с 8 по 12:

|Переменная| Тип |  Описание |
|--|--|--|
| `tg_bot_token` | str | Токен телеграм бота, берём у BotFather|
| `chat_id` | int |Id чата или юзера, куда будут приходить вулны |
| `api_key` | str | Токен API акунетикса, берем из настроек аку|
| `host` | str | URL до твоего акунетикса, `https://ip:port` |

## Примечание

### Ну да, нагавнокодил малёха, и что с того? 
#### Идеи/предложения приветствуются.
