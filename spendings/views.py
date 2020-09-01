from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from . import filters
from . import models
from . import serializers


class SpendingViewSetForUser(viewsets.ModelViewSet):
    queryset = models.Spending.objects.all()
    serializer_class = serializers.SpendingSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filterset_class = filters.SpendingFilter
    ordering_fields = '__all__'
