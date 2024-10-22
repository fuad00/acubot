from aiogram import Router, F
from aiogram.types import Message
import asyncio
from modules import api
import uuid
from aiogram.exceptions import TelegramBadRequest

router = Router()





@router.message(F.text)
async def anymsg(message: Message) -> None:
    """
    Answer to any message
    """
    
    await message.answer('/start')