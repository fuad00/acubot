
#!/usr/bin/python3
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


from config import BOT_TOKEN
from handlers import commands, anymsg, callbacks
from middlewares.UserFilter import UserFilterMiddleware


# All handlers should be attached to the Router (or Dispatcher)

### BOTFATHER SETTINGS ###
"""
https://t.me/BotFather > /mybots > select your bot > Edit Commamds >

menu - Главная

"""

dp = Dispatcher(storage=MemoryStorage())

# Initialize Bot instance with default bot properties which will be passed to all API calls
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    # middlewares for all handlers (routes)
    dp.message.middleware(UserFilterMiddleware(bot))
    dp.callback_query.middleware(UserFilterMiddleware(bot))

    dp.include_routers(commands.router, anymsg.router)

    dp.include_routers(
        # main buttons
        callbacks._menu, callbacks._settings,
        )




    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())