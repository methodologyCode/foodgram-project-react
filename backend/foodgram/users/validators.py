import re

from django.core.exceptions import ValidationError


def validate_username(value):
    regex = r'^[\w.@+-]+\Z'

    if value.lower() == 'me':
        raise ValidationError(
            'Недопустимое имя пользователя!'
        )

    if not re.match(regex, value):
        raise ValidationError(
            'Некорректные символы в username!'
        )

    return value
