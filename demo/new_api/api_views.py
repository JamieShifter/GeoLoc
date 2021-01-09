from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from new_api.serializers import Location_serializer
from new_api.models import Location



class Ip_GeoLocation(ListAPIView):
    permission_classes = (IsAuthenticated, )

    queryset = Location.objects.all()
    serializer_class = Location_serializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('ip', 'city')


class GeolocationCreate(CreateAPIView):
    serializer_class = Location_serializer

    def create(self, request, *args, **kwargs):
        try:
            ip = request.data.get('ip')
            if ip is not None and ip != "0.0.0.0":
                raise ValidationError({'ip': 'ip must be different than 0.0.0.0'})
        except ValueError:
            raise ValidationError({'ip': 'Valid IP address must be provided'})
        return super().create(request, *args, **kwargs)


class GeolocationRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    lookup_field = 'id'
    serializer_class = Location_serializer

    def delete(self, request, *args, **kwargs):
        loc_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('location_data_{}'.format(loc_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            loc = response.data
            cache.set('location_data_{}'.format(loc['id']),{
                'id': loc['id'],
                'ip': loc['ip'],
                'ip_type': loc['ip_type'],
                'continent_code': loc['continent_code'],
                'continent_name': loc['continent_name'],
                'country_code': loc['country_code'],
                'country_name': loc['country_name'],
                'region_code': loc['region_code'],
                'region_name': loc['region_name'],
                'city': loc['city'],
                'zip': loc['zip'],
                'latitude': loc['latitude'],
                'longitude': loc['longitude'],
                'geoname_id': loc['geoname_id'],
                'capital': loc['capital'],
                'language_code': loc['language_code'],
                'language_name': loc['language_name'],
                'native_language_name': loc['native_language_name'],
                'country_flag': loc['country_flag'],
                'country_flag_emoji': loc['country_flag_emoji'],
                'country_flag_emoji_unicode': loc['country_flag_emoji_unicode'],
                'calling_code': loc['calling_code'],
                'is_eu': loc['is_eu'],
            })
            return response




