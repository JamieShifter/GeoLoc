from django.db import models

# Create your models here.


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=100)
    ip_type = models.CharField(max_length=10)
    continent_code = models.CharField(max_length=100)
    continent_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    region_code = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geoname_id = models.CharField(max_length=100, default='')
    capital = models.CharField(max_length=100, default='')
    language_code = models.CharField(max_length=100, default='')
    language_name = models.CharField(max_length=100, default='')
    native_language_name = models.CharField(max_length=100, default='')
    country_flag = models.CharField(max_length=100, default='')
    country_flag_emoji = models.CharField(max_length=100, default='')
    country_flag_emoji_unicode = models.CharField(max_length=100, default='')
    calling_code = models.CharField(max_length=100, default='')
    is_eu = models.CharField(max_length=100, default='')
    time_zone = models.TextField(default='')
    currency = models.TextField(default='')
    connection = models.TextField(default='')

    def __str__(self):
        return self.ip