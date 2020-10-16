import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from squirrel.models import Sightings

class Command(BaseCommand):
    help = "importing squirrel"

    def add_arguments(self, parser):
        parser.add_argument('sq_file', help = "file containing squirrel data")

    def handle(self, *args, **options):
        file_ = options['sq_file']

        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                obj = Sightings()
                obj.latitude = item['X']
                obj.longitude= item['Y']
                obj.uniqueId= item['Unique Squirrel ID']
                obj.shift= item['Shift']
                obj.date = datetime.strptime(str(item['Date']),'%m%d%Y')
                obj.age = item['Age']
                
                obj.save()

            msg = f'importing from {file_}'
            
            self.stdout.write(self.style.SUCCESS(msg))
