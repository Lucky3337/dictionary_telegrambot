from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger
from tortoise import Tortoise

import config
from app import middlewares
from app import handlers

storage = MemoryStorage()
telegram_bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(telegram_bot, storage=storage)


def on_startup():
    logger.info("Register handlers...")
    # Register you handlers here.
    handlers.default.setup(dp)
    dp.middleware.setup(middlewares.UserMiddleware())


async def database_init():
    await Tortoise.init(
        db_url=config.DB_URL,
        modules={
            'models': ['app.models']
        }
    )
    # await Tortoise.init_models(app_label='models', models_paths=['app.models'])
    await Tortoise.generate_schemas(True)
    logger.info("Tortoise inited!")


if __name__ == "__main__":
    on_startup()
    dp.loop.create_task(database_init())
    executor.start_polling(dp, skip_updates=True)