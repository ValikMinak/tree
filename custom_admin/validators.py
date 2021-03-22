from django.core.exceptions import ValidationError


def validate_domainonly_email(value):
    if not 'lalala' in value:
        raise ValidationError("Sorry email submitted is not valid")
    return value
