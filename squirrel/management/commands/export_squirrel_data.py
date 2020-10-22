import csv
from django.core.management.base import BaseCommand
from squirrel.models import Sightings

class Command(BaseCommand):
    help = "exporting squirrel"
    def handle(self, *args, **options):
        with open("export.csv", 'w', newline = '') as csvfile:
            fieldnames = ['latitude', 'longitude', 'uniqueId', 'shift', 'date', 'age']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for obj in Sightings.objects.all():
                writer.writerow({'latitude':obj.latitude,'longitude':obj.longitude, 'uniqueId' : obj.uniqueId, 'shift':obj.shift, 'date': obj.date, 'age': obj.age })
