from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Sightings

def map(request):
        sightings = Sightings.objects.all()[:100]
        context = {'sightings' :sightings}
        return render (request, 'squirrel/map.html', context)

