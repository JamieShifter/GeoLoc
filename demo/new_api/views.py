from django.shortcuts import render
from django.http import HttpResponse
from new_api.models import Location

def index(request):
    context = {
        'locations' : Location.objects.all(),
    }
    return render(request, '')