from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Значение "%(value)s" состоит из  %(show_value)d символов! Должно быть не менее %(limit_value)d.'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


FORBIDDEN_WORDS = ['винни-пух', 'тайвань-независимый', "гонконг-наш!"]

def validate_forbidden_words(value):
    text = value.lower()

    for word in FORBIDDEN_WORDS:
        if word in text:
            raise ValidationError(f'Фраза «{word}» запрещена! -1 000 000 очков партии.')