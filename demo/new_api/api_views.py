from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from new_api.serializers import Location_serializer
from new_api.models import Location


class Location_Pagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class IP_GeoLocation(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = Location_serializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('ip', 'city')
    pagination_class = Location_Pagination


