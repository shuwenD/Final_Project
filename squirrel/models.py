from django.db import models
from django.utils.translation import gettext as _
  
class Sightings(models.Model):
    longtitude = models.FloatField(
            )
    latitude = models.FloatField(
            )
    uniqueId = models.CharField(
            max_length = 100,
            )
    PM = 'pm'
    AM = 'am'

    SHIFT_CHOICES = [
            (PM,'PM'),
            (AM,'AM'),
            ]
    shift = models.CharField(
            max_length = 100,
            choices = SHIFT_CHOICES,
            )
    date = models.DateField(
            )
    Adult = 'adult'
    Juvenile = 'juvenile'
    AGE_CHOICES = [
            (Adult, 'Adult'),
            (Juvenile,'Juvenile'),
            ]
    age = models.CharField(
            max_length = 100,
            choices = AGE_CHOICES,
            )
    # def __str__(self):
    #     return self.uniqueId 


