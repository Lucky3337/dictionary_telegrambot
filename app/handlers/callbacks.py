from loguru import logger
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app.data.messages import english_word_menu, main_menu_message
from app.data.states import MainForm, EnglishForm
from app.services.words import save_new_english_word


async def main_menu_callback(query: CallbackQuery, state: FSMContext):
    if query.data == 'MainMenu:englishword':
        await english_word_menu(query)
    elif query.data == 'MainMenu:russianword':
        await MainForm.russian.set()
    elif query.data == 'MainMenu:myvocabulary':
        await MainForm.vocabulary.set()


async def english_menu_callback(query: CallbackQuery, state: FSMContext):
    if query.data == 'EnglishWordMenu:back':
        """Press button back to main menu"""
        await main_menu_message(query.from_user.id)
    elif query.data == 'EnglishWordMenuEnterEnglishWord:back':
        await english_word_menu(query)
    elif query.data == 'EnglishWordMenuEnterRussianWord:back':
        await english_word_menu(query)
    elif query.data == 'EnglishWordMenuEnterRussianWord:ready':
        data = await state.get_data()
        user_id = query.from_user.id
        await save_new_english_word(data, user_id)
        await state.finish()
        await main_menu_message(query.from_user.id)
