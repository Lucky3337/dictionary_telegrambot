from tortoise import Model, fields


class TimestampMixin:
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class AbstractBaseModel(Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True


class User(AbstractBaseModel, TimestampMixin):
    telegram_id = fields.IntField(unique=True)
    date_created = fields.DatetimeField(auto_now_add=True)


class EnglishWord(AbstractBaseModel, TimestampMixin):
    """Words are english"""
    word = fields.CharField(max_length=120, unique=True)


class UserWord(AbstractBaseModel, TimestampMixin):
    """Words of user"""
    user = fields.ForeignKeyField('models.User', on_delete=fields.CASCADE, related_name='users')
    pair_words = fields.ForeignKeyField("models.Translation", on_delete=fields.CASCADE)


class Translation(AbstractBaseModel, TimestampMixin):
    """Translation pair"""
    english_word = fields.ForeignKeyField("models.EnglishWord", on_delete=fields.CASCADE)
    russian_word = fields.ForeignKeyField("models.TranslationEnglishWord", on_delete=fields.CASCADE)


class TranslationEnglishWord(AbstractBaseModel, TimestampMixin):
    """Translations for english words"""
    id = fields.IntField(pk=True)
    russian_translation = fields.CharField(max_length=120, unique=True)


__all__ = ['User', 'EnglishWord', 'UserWord', 'TranslationEnglishWord']
