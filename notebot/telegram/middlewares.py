import logging

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from notebot.models import User

logger = logging.getLogger(__name__)


class ACLMiddleware(BaseMiddleware):
    async def setup_chat(self, data: dict, user: types.User, message: types.Message):
        user_id = user.id

        user = (
            await User.get_or_create(
                id=user_id,
                defaults={
                    "username": user.username,
                    "full_name": user.full_name,
                    "language": user.language_code,
                    "is_active": True,
                    "role": "user",
                }
            )
        )[0]

        data["user"] = user

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user, message)


class LoggerMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        logger.info(f"{message.from_user.full_name} {message.text}", extra=data)

