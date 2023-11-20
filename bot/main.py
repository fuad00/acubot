import asyncio
import logging
from config import BOT_TOKEN
from modules import handlers, callbacks, middlewares
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)       # Logging
bot = Bot(token=BOT_TOKEN, parse_mode="HTML") # Bot object
dp = Dispatcher()                             # Dispatcher

async def main():
    dp.update.middleware.register(middlewares.NewUserMiddleware())  # Middleware checks if user allowed to use this bot
    dp.message.register(handlers.start,   Command('start'))  # Handle '/start' command
    dp.message.register(handlers.anymsg, F.text)  # Handle any text

    await dp.start_polling(bot)  # Start polling

asyncio.run(main())