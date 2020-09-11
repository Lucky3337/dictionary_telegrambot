from typing import Dict, Union, List

from app.models import EnglishWord, TranslationEnglishWord, Translation, UserWord, User


async def save_new_english_word(data: Dict[str, Union[str, List]], user_id: int) -> bool:
    """Save a new english word in DB
    data: {'english_word': 'apple', 'russian_words': ['яблоко']}"""
    english_word = await EnglishWord.create(word=data['english_word'])
    user = await User.get(telegram_id=user_id)
    for word in data['russian_words']:
        russian_translation = await TranslationEnglishWord.create(russian_translation=word)
        translation = await Translation.create(
            english_word=english_word,
            russian_word=russian_translation
        )
        await UserWord.create(
            user=user,
            pair_words=translation
        )
