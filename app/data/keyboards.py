from aiogram.utils.callback_data import CallbackData

from .mixins import ActionsMixin
from app.utils.singleton import singleton_class


@singleton_class
class MainMenu(ActionsMixin):
    """This class consist of text buttons of main menu"""
    def __init__(self):
        self.parent = None
        self.data = (
            ('englishword', 'English word'),
            ('russianword', 'Russian word'),
            ('myvocabulary', 'My vocabulary'),
        )
        self.prefix = 'MainMenu'
        self.callback_data = CallbackData(self.prefix, 'action')


@singleton_class
class EnglishWordMenu(ActionsMixin):
    """This class consist of text buttons of englishword menu"""
    def __init__(self):
        self.parent = MainMenu()
        self.data = (
            ('back', 'back'),
        )
        self.prefix = 'EnglishWordMenu'
        self.callback_data = CallbackData(self.prefix, 'action')


@singleton_class
class EnglishWordMenuEnterEnglishWord(ActionsMixin):
    """This class consist of text buttons of englishword menu when writing english word"""
    def __init__(self):
        self.parent = MainMenu()
        self.data = (
            ('back', 'back'),
        )
        self.prefix = 'EnglishWordMenuEnterEnglishWord'
        self.callback_data = CallbackData(self.prefix, 'action')


@singleton_class
class EnglishWordMenuEnterRussianWord(ActionsMixin):
    """This class consist of text buttons of englishword menu when writing russian word"""
    def __init__(self):
        self.parent = EnglishWordMenu()
        self.data = (
            ('back', 'back'),
            ('ready', 'ready'),
        )
        self.prefix = 'EnglishWordMenuEnterRussianWord'
        self.callback_data = CallbackData(self.prefix, 'action')