from django.forms import ModelForm
from .models import Sightings

class SightingForm(ModelForm):
    class Meta:
        model = Sightings
        fields = ['longitude', 'latitude', 'uniqueId', 'shift', 'date', 'age']

