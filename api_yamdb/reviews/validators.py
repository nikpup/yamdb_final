from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    """Year of masterpiece cannot be bigger than today."""
    now = timezone.now().year
    if value > now:
        raise ValidationError(
            f'{value} не может быть больше {now}'
        )


def validate_username(value):
    """User name cannot be ME."""
    if value == 'me':
        raise ValidationError(
            ('Имя пользователя не может быть <me>.'),
            params={'value': value},
        )
