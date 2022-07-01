from django.utils import timezone
from rest_framework.serializers import ValidationError


def valid_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            f'Год не может быть больше {timezone.now().year}'
        )
    return value
