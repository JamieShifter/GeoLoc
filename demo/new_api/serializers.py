from rest_framework import serializers

from new_api.models import Location

class Location_serializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'ip', 'ip_type', 'continent_code', 'continent_name', 'country_code', 'country_name',
                  'region_code', 'region_name', 'city', 'zip', 'latitude', 'longitude', 'geoname_id',
                  'capital', 'language_code', 'language_name', 'native_language_name', 'country_flag',
                  'country_flag_emoji', 'country_flag_emoji_unicode', 'calling_code', 'is_eu',
                  'time_zone', 'currency', 'connection')
