from aiogram import BaseMiddleware, types, Bot
from modules import api 
from typing import Callable, Dict, Any, Awaitable, List
from modules import BTN
from aiogram.exceptions import TelegramBadRequest



class UserFilterMiddleware(BaseMiddleware):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    async def __call__(
        self,
        handler: Callable[[types.Update, Dict[str, Any]], Awaitable[Any]],
        event: types.Update,
        data: Dict[str, Any]
    ) -> Any:
        user_id = None
        first_name = None
        last_name = None
        nickname = None

        if isinstance(event, types.Message):
            user_id = event.from_user.id
            first_name = event.from_user.first_name
            last_name = event.from_user.last_name
            nickname = event.from_user.username
        elif isinstance(event, types.CallbackQuery):
            user_id = event.from_user.id
            first_name = event.from_user.first_name
            last_name = event.from_user.last_name
            nickname = event.from_user.username



        return await handler(event, data)
