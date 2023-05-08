import re

from django.core.exceptions import ValidationError


def validate_slug(value):
    regex = r'^[-a-zA-Z0-9_]+$'

    if not re.match(regex, value):
        raise ValidationError(
            'Некорректный слаг'
        )

    return value


def validate_color(value):
    regex = r'^#[A-Fa-f0-9]{6}$'

    if not re.match(regex, value):
        raise ValidationError(
            'Некорректный цвет'
        )

    return value
