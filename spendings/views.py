from rest_framework import viewsets

from . import models
from . import serializers


class SpendingViewSetForUser(viewsets.ModelViewSet):
    queryset = models.Spending.objects.all()
    serializer_class = serializers.SpendingSerializer
