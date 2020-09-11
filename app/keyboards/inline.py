from typing import Tuple
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loguru import logger


class MenuInlineButtons:
    """Menu of inline buttons
    Example of data: (
            ("callback_data", 'some_text'),
            ("callback_data", 'some_another_text'),
        )
    """
    row_width: int
    data: Tuple[Tuple[str, str]]
    prefix: str
    callback_data: CallbackData

    def __init__(self, row_width, data, prefix, callback_data):
        self.row_width = row_width
        self.data = data
        self.prefix = prefix
        self.callback_data = callback_data

    @property
    def buttons(self):
        keyboard_markup = InlineKeyboardMarkup(row_width=self.row_width)
        row_btns = (InlineKeyboardButton(
            text,
            callback_data=self.callback_data.new(action=callback_data_str)
        ) for callback_data_str, text in self.data)
        keyboard_markup.row(*row_btns)
        return keyboard_markup
