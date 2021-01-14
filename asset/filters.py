import django_filters

from .models import *

class Filter(django_filters.FilterSet):
    class Meta:
        model = TheViewAsset
        fields = '__all__'