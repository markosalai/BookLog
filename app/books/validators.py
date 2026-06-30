import re
from django.core.exceptions import ValidationError


def validiraj_isbn(isbn):
    if not isbn:
        raise ValidationError('ISBN je obavezan')
    # remove dashes and spaces
    cleaned = re.sub(r'[\s-]', '', isbn)
    if len(cleaned) not in (10, 13):
        raise ValidationError('ISBN mora imati 10 ili 13 znakova')
    if not cleaned[:-1].isdigit():
        raise ValidationError('ISBN nije validan format')


def validiraj_godinu(godina):
    if not godina:
        raise ValidationError('Godina izdanja je obavezna')
    try:
        godina = int(godina)
    except (TypeError, ValueError):
        raise ValidationError('Godina izdanja mora biti broj')
    if godina < 1000 or godina > 2025:
        raise ValidationError('Godina izdanja mora biti između 1000 i 2025')


def validiraj_ocjenu(ocjena):
    if ocjena is None:
        raise ValidationError('Ocjena je obavezna')
    try:
        ocjena = int(ocjena)
    except (TypeError, ValueError):
        raise ValidationError('Ocjena mora biti broj')
    if ocjena < 1 or ocjena > 5:
        raise ValidationError('Ocjena mora biti između 1 i 5')


def validiraj_knjigu(data):
    errors = {}
    try:
        validiraj_isbn(data.get('isbn'))
    except ValidationError as e:
        errors['isbn'] = str(e.message)

    try:
        validiraj_godinu(data.get('godina_izdanja'))
    except ValidationError as e:
        errors['godina_izdanja'] = str(e.message)

    if not data.get('naslov', '').strip():
        errors['naslov'] = 'Naslov je obavezan'

    if not data.get('autor', '').strip():
        errors['autor'] = 'Autor je obavezan'

    return errors