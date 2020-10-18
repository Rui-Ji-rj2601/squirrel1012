from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Latitude = models.FloatField()

    Longitude = models.FloatField()

    Unique_Squirrel_ID = models.CharField(
        max_length=20,
        primary_key=True,
        default=None
    )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICE = [
        (AM, _('AM')),
        (PM, _('PM')),
    ]

    Shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICE
    )

    Date = models.DateField()

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICE = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
    ]

    Age = models.CharField(
        max_length=15,
        choices=AGE_CHOICE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.Unique_Squirrel_ID

# Create your models here.
