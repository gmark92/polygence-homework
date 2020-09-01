from django_filters import rest_framework as filters


class SpendingFilter(filters.FilterSet):
    currency = filters.CharFilter(field_name='currency')
