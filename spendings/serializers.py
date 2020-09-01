from rest_framework import serializers

from . import models


class SpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spending
        fields = ('date', 'amount', 'currency', 'description',)
