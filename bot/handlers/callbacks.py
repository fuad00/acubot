from aiogram import Router, F, html
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from modules import messages, logic
from middlewares.AdminFilter import AdminFilterMiddleware



_menu = Router()



_menu.callback_query.middleware(AdminFilterMiddleware(refresh_interval=3))
# Define the callback data factory for structured callback query data


# [⚙️ Settings]
@_menu.callback_query(F.data.startswith("settings_menu "))
async def func(call: CallbackQuery, is_admin: bool):
    pass

# [💭 Help]
@_menu.callback_query(F.data.startswith("help_menu "))
async def func(call: CallbackQuery):
    # soon
    pass

    




_settings = Router()


