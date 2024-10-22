from aiogram import BaseMiddleware, types
from modules import api
import time
import asyncio
from typing import Callable, Dict, Any, Awaitable

class AdminFilterMiddleware(BaseMiddleware):
    def __init__(self, refresh_interval: int = 1):  # refresh rate in seconds
        super().__init__()
        self.admin_ids = []
        self.last_update = 0
        self.refresh_interval = refresh_interval

    async def get_admin_ids(self):
        r = await api.get_superadmins()

        self.admin_ids = r['admin_ids']
        self.last_update = time.time()

    async def __call__(
        self,
        handler: Callable[[types.Update, Dict[str, Any]], Awaitable[Any]],
        event: types.Update,
        data: Dict[str, Any]
    ) -> Any:
        # Initial fetch if not done yet
        if not self.admin_ids:
            await self.get_admin_ids()

        # Refresh admin IDs if the refresh interval has passed
        if time.time() - self.last_update > self.refresh_interval:
            await self.get_admin_ids()

        
        if event.message:
            user_id = event.message.chat.id
        elif event.callback_query:
            user_id = event.callback_query.chat.id
        else:
            return await handler(event, data)


        if user_id in self.admin_ids:
            data['is_admin'] = True
            data['admin_tgid'] = user_id
        else:
            data['is_admin'] = False
            data['admin_tgid'] = user_id

        return await handler(event, data)
