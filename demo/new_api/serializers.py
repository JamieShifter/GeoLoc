from rest_framework import serializers

from new_api.models import Location

class Location_serializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'ip', 'ip_type', 'continent_code', 'continent_name', 'country_code', 'country_name',
                  'reqion_code', 'region_name', 'city', 'zip', 'latitude', 'longitude', 'location', 'time_zone',
                  'currency', 'connection')
