import re

from django.core.exceptions import ValidationError


def validate_slug(value):
    regex = r'^[-a-zA-Z0-9_]+$'

    if not re.match(regex, value):
        raise ValidationError(
            'Некорректный слаг'
        )

    return value
