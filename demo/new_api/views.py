from django.shortcuts import render, redirect
from new_api.models import Location
from django.http import JsonResponse
import requests


def get_public_ip():
    return requests.get('https://api.ipify.org').text


def redirect_view(request):
    response = redirect("http://api.ipstack.com/%s?access_key=28c21d3b10b7d8a4cff5172f1f8727c8" % get_public_ip())
    return response


def home(request):
    return render(request, 'new_api/home.html')


def get_local(request, ip_address=None):
    url_ip = ip_address if ip_address != None else get_public_ip()
    response = requests.get(('http://api.ipstack.com/%s?access_key=28c21d3b10b7d8a4cff5172f1f8727c8' % url_ip))
    data = response.json()
    location_data = Location(
        ip=data['ip'],
        ip_type=data['type'],
        continent_code=data['continent_code'],
        continent_name=data['continent_name'],
        country_code=data['country_code'],
        country_name=data['country_name'],
        region_code=str(data['region_code']),
        region_name=data['region_name'],
        city=data['city'],
        zip=str(data['zip']),
        latitude=str(data['latitude']),
        longitude=str(data['longitude']),
        geoname_id=str(data['location']['geoname_id']),
        capital=str(data['location']['capital']),
        language_code=str(data['location']['languages'][0]['code']),
        language_name=str(data['location']['languages'][0]['name']),
        native_language_name=str(data['location']['languages'][0]['native']),
        country_flag=str(data['location']['country_flag']),
        country_flag_emoji=str(data['location']['country_flag_emoji']),
        country_flag_emoji_unicode=str(data['location']['country_flag_emoji_unicode']),
        calling_code=str(data['location']['calling_code']),
        is_eu=str(data['location']['is_eu']),
    )
    location_data.save()
    return render(request, 'new_api/submitted.html', {'url_ip': url_ip})


def error_404(request, exception):
    message = ('The endpoint is not found')
    response = JsonResponse(data={'message': message, 'status_code': 404})
    response.status_code = 404
    return response


def error_500(request):
    message = ('Internal error occured')
    response = JsonResponse(data={'message': message, 'status_code': 500})
    response.status_code = 500
    return response