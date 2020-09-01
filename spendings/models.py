from django.core.validators import MinValueValidator, MaxLengthValidator
from django.db import models

from spendings import currency as c


class Spending(models.Model):
    date = models.DateTimeField(blank=True, null=False)
    amount = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    currency = models.CharField(
        max_length=3, choices=c.CURRENCY_CHOICES, default=c.DEFAULT_CURRENCY)
    description = models.TextField(blank=True, null=True, validators=[
                                   MaxLengthValidator(280)])

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
