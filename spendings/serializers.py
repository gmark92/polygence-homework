from rest_framework import serializers

from . import models


class SpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spending
        fields = ('id', 'date', 'amount', 'currency', 'description',)
        read_only_fields = ['id']
