from aiogram.dispatcher.filters.state import State, StatesGroup


class MainForm(StatesGroup):
    english = State()
    russian = State()
    myself = State()
    vocabulary = State()


class EnglishForm(StatesGroup):
    write_english = State()
    write_russian = State()

