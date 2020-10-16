from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Sightings

def map(request):
        sightings = Sightings.objects.all()[:100]
        context = {'sightings' :sightings}
        return render (request, 'squirrel/map.html', context)

def list(request):
	sightings = Sightings.objects.all()
	context = {'sightings' : sightings}
	return render (request, 'squirrel/list.html', context)
def detail(request, sight_id):
    sightings = get_object_or_404(Sightings, pk=sight_id)
    context = {'sightings' : sightings}
    return render (request, 'squirrel/detail.html', context)

def add(request):
    # to be continued
    pass
