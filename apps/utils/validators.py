from django.core import validators


class NationalIdValidator(validators.RegexValidator):
    regex = r"^\d{11}$"
    message = "National ID must be a string of 11 digits."
    flags = 0
