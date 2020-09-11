from aiogram import Dispatcher
from aiogram.utils.exceptions import MessageNotModified
from loguru import logger

from .login import login_test
from .start import start_cmd
from app.handlers.callbacks import main_menu_callback, english_menu_callback
from app.handlers.messages import write_english_word_message_handler, write_russian_word_message_handler
from app.data.keyboards import MainMenu, EnglishWordMenu, EnglishWordMenuEnterRussianWord
from app.data.states import MainForm, EnglishForm


def setup(dp: Dispatcher):
    """Commands handlers"""
    dp.register_message_handler(start_cmd, commands=['start'])
    dp.register_message_handler(login_test, commands=['login'])

    """Callback handlers"""
    main_menu = MainMenu()
    dp.register_callback_query_handler(
        main_menu_callback,
        lambda callback_query: main_menu.callback_data.filter(action=main_menu.actions),
        state=MainForm.myself
    )
    english_word_menu = EnglishWordMenu()
    dp.register_callback_query_handler(
        english_menu_callback,
        lambda callback_query: english_word_menu.callback_data.filter(action=english_word_menu.actions),
        state=[MainForm.english, EnglishForm, EnglishWordMenuEnterRussianWord]
    )

    """Message handlers"""
    dp.register_message_handler(write_english_word_message_handler, state=EnglishForm.write_english)
    dp.register_message_handler(write_russian_word_message_handler, state=EnglishForm.write_russian)

    """Error handlers"""
    @dp.errors_handler(exception=MessageNotModified)  # handle the cases when this exception raises
    async def message_not_modified_handler(update, error):
        return True  # errors_handler must return True if error was handled correctly