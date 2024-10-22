from aiogram.types import Message, CallbackQuery
from inspect import cleandoc as clear
from modules import BTN
from main import bot

async def menu(event: Message | CallbackQuery) -> None:
    text = clear('''
        Welcome!
    ''')

    if isinstance(event, CallbackQuery):
        tgid = event.message.chat.id
        await event.message.edit_text(text, reply_markup=BTN.menu(tgid))
    else:
        tgid = event.chat.id
        await event.answer(text, reply_markup=BTN.menu(tgid))
