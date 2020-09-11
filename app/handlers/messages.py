from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data.keyboards import EnglishWordMenu, EnglishWordMenuEnterRussianWord, EnglishWordMenuEnterEnglishWord
from app.data.states import EnglishForm
from app.data.texts import ENTER_RUSSIAN_WORD, ENTER_MORE_RUSSIAN_WORD
from app.keyboards.inline import MenuInlineButtons
from bot import telegram_bot

from loguru import logger


async def write_english_word_message_handler(message: Message, state: FSMContext):
    await state.set_data({
        "english_word": message.text
    })
    menu = EnglishWordMenuEnterEnglishWord()
    menu_inline = MenuInlineButtons(
        row_width=3,
        data=menu.data,
        prefix=menu.prefix,
        callback_data=menu.callback_data
    )
    await message.reply(ENTER_RUSSIAN_WORD, reply_markup=menu_inline.buttons)
    await EnglishForm.write_russian.set()


async def write_russian_word_message_handler(message: Message, state: FSMContext):
    logger.debug(f"message2 {message.text}")
    data = await state.get_data()
    logger.debug(f"data {data}")
    if data.get("russian_words"):
        data["russian_words"].append(message.text)
        await state.update_data({
            "russian_words": data["russian_words"]
        })
    else:
        await state.update_data({
            "russian_words": [message.text]
        })
    menu = EnglishWordMenuEnterRussianWord()
    menu_reply = MenuInlineButtons(
        row_width=3,
        data=menu.data,
        prefix=menu.prefix,
        callback_data=menu.callback_data
    )
    await message.reply(
        text=ENTER_MORE_RUSSIAN_WORD,
        reply_markup=menu_reply.buttons
    )