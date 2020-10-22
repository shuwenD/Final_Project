from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import SightingForm
from .models import Sightings

def map(request):
        sightings = Sightings.objects.all()[:100]
        context = {'sightings' :sightings}
        return render (request, 'squirrel/map.html', context)
def list(request):
        sightings = Sightings.objects.all()
        context = {'sightings' : sightings}
        return render (request, 'squirrel/list.html', context)
def add(request):
    context ={}
    form = SightingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/sightings')
    context['form']= form
    return render(request,'squirrel/add.html',context)

def update(request,sight_id):
    context ={}
    instance = Sightings.objects.filter(uniqueId =sight_id).first()
    form = SightingForm(instance=instance)
    if form.is_valid():
    	form.save()
    	return HttpResponseRedirect('/sightings')
    context['form']= form
    return render(request,'squirrel/update.html',context)
