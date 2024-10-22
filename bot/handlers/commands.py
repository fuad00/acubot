from aiogram import Router, F, html
from aiogram.filters import Command
from aiogram.types import Message
from modules import messages

router = Router()





    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    # html.bold or html.qoute makes text much safer
    # await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")






@router.message(Command("start"))
async def func(message: Message) -> None:
    """
    Answer to `/start` command
    """
    await messages.menu(message)


@router.message(Command("menu"))
async def func(message: Message) -> None:
    """
    Answer to `/menu` command
    """
    await messages.menu(message)

