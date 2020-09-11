from aiogram.types import Message
from loguru import logger

from app.data.keyboards import MainMenu
from app.data.messages import main_menu_message
from app.data.texts import MAIN_MENU
from app.keyboards.inline import MenuInlineButtons
from app.data.states import MainForm
from bot import telegram_bot


async def start_cmd(msg: Message):
    logger.info(f"{msg.from_user.full_name} send /start")
    await main_menu_message(msg.from_user.id)