
from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import (
    CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message,
)


def menu(tgid):
    btn1 = InlineKeyboardButton(text='⚙️ Settings', callback_data=f'settings_menu {tgid}')
    btn2 = InlineKeyboardButton(text='💭 Help me', callback_data=f"help_main {tgid}")
    buttons = [
        [btn1, btn2],
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def back_to_menu(tgid):
    btn1 = InlineKeyboardButton(text='🏠 Menu', callback_data=f"back_to_menu {tgid}")
    buttons = [
        [btn1]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


