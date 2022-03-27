from tortoise import Tortoise
from notebot.db.config import TORTOISE_ORM
from aiogram.utils.executor import Executor
from aiogram import Dispatcher
from aiogram.dispatcher.webhook import get_new_configured_app, BOT_DISPATCHER_KEY
from aiohttp import web
from aiohttp.web_app import Application

from notebot.telegram.middlewares import ACLMiddleware, LoggerMiddleware
from notebot.telegram.app import bot
from notebot import settings

import logging
import sys

fmt = logging.Formatter(
    fmt=settings.LOG_FORMAT,
    datefmt=settings.LOG_DATE_FORMAT,
)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(settings.LOG_LEVEL)
sh.setFormatter(fmt)
logger = logging.getLogger(__name__)
logger.setLevel(settings.LOG_LEVEL)
logger.addHandler(sh)

# will print debug sql
logger_db_client = logging.getLogger("db_client")
logger_db_client.setLevel(settings.LOG_LEVEL)
logger_db_client.addHandler(sh)

logger_tortoise = logging.getLogger("tortoise")
logger_tortoise.setLevel(settings.LOG_LEVEL)
logger_tortoise.addHandler(sh)


async def init(dp: Dispatcher):
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        config=TORTOISE_ORM,
    )

    dp.middleware.setup(ACLMiddleware())
    dp.middleware.setup(LoggerMiddleware())


async def on_startup(application: Application):
    dp = application[BOT_DISPATCHER_KEY]
    await init(dp)

    webhook = await bot.get_webhook_info()
    if webhook.url != settings.TELEGRAM_WEBHOOK_URL:
        await bot.delete_webhook()
        await bot.set_webhook(url=settings.TELEGRAM_WEBHOOK_URL)
        logging.info("Webhook set")

if __name__ == '__main__':
    from notebot.telegram import dispatcher

    executor = Executor(dispatcher)

    executor.on_startup(init)

    if settings.TELEGRAM_WEBHOOK_ENABLED:
        logger.info("Webhook enabled")
        app = get_new_configured_app(dispatcher)
        app.on_startup.append(on_startup)
        web.run_app(app, host=settings.TELEGRAM_INTERNAL_HOST, port=settings.TELEGRAM_INTERNAL_PORT)
    else:
        logger.info("Polling enabled")
        executor.start_polling()
