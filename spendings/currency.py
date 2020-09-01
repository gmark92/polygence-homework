import pycountry

CURRENCY_CHOICES = []

for c in pycountry.currencies:
    curr_code = c.alpha_3
    curr_name = c.name
    CURRENCY_CHOICES.append((curr_code, curr_name))

DEFAULT_CURRENCY = 'HUF'
