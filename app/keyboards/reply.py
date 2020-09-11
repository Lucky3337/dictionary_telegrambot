from typing import Tuple
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loguru import logger


class MenuReplyButtons:
    """Menu of inline buttons
    Example of data: (
            ("callback_data", 'some_text'),
            ("callback_data", 'some_another_text'),
        )
    """
    row_width: int
    data: Tuple[Tuple[str, str]]

    def __init__(self, row_width, data):
        self.row_width = row_width
        self.data = data

    @property
    def buttons(self):
        keyboard_markup = ReplyKeyboardMarkup(
            row_width=self.row_width,
            resize_keyboard=True
        )
        row_btns = (KeyboardButton(text) for callback_data_str, text in self.data)
        keyboard_markup.row(*row_btns)
        return keyboard_markup