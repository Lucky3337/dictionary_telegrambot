from aiogram.types import CallbackQuery, Message

from app.data.keyboards import EnglishWordMenu, MainMenu, EnglishWordMenuEnterEnglishWord
from app.data.states import MainForm, EnglishForm
from app.data.texts import ENTER_ENGLISH_WORD, MAIN_MENU, ENTER_RUSSIAN_WORD
from app.keyboards.inline import MenuInlineButtons
from bot import telegram_bot


async def english_word_menu(query: CallbackQuery):
    menu = EnglishWordMenu()
    menu_inlines = MenuInlineButtons(
        row_width=3,
        data=menu.data,
        prefix=menu.prefix,
        callback_data=menu.callback_data
    )
    await telegram_bot.send_message(
        chat_id=query.from_user.id,
        text=ENTER_ENGLISH_WORD,
        reply_markup=menu_inlines.buttons
    )
    await MainForm.english.set()
    await EnglishForm.write_english.set()


async def main_menu_message(user_id: int):
    await MainForm.myself.set()
    menu = MainMenu()
    menu_inlines = MenuInlineButtons(
        row_width=3,
        data=menu.data,
        prefix=menu.prefix,
        callback_data=menu.callback_data
    )
    await telegram_bot.send_message(
        chat_id=user_id,
        text=MAIN_MENU,
        reply_markup=menu_inlines.buttons
    )


async def enter_russian_word_message(message: Message):
    menu = EnglishWordMenuEnterEnglishWord()
    menu_inline = MenuInlineButtons(
        row_width=3,
        data=menu.data,
        prefix=menu.prefix,
        callback_data=menu.callback_data
    )
    await message.reply(ENTER_RUSSIAN_WORD, reply_markup=menu_inline.buttons)
    await EnglishForm.write_russian.set()
