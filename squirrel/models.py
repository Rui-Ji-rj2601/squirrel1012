from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Longitude = models.FloatField()

    Latitude = models.FloatField()

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

    Primary_Fur_Color = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )

    Location = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )

    Specific_Location = models.CharField(
        max_length=45,
        null=True,
        blank=True,
    )

    Running = models.BooleanField(default=False)
    Chasing = models.BooleanField(default=False)
    Climbing = models.BooleanField(default=False)
    Eating = models.BooleanField(default=False)
    Foraging = models.BooleanField(default=False)

    Other_Activities = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    Kuks = models.BooleanField(default=False)
    Quaas = models.BooleanField(default=False)
    Moans = models.BooleanField(default=False)
    Tail_flags = models.BooleanField(default=False)
    Tail_twitches = models.BooleanField(default=False)
    Approaches = models.BooleanField(default=False)
    Indifferent = models.BooleanField(default=False)
    Runs_from = models.BooleanField(default=False)

    def __str__(self):
        return self.Unique_Squirrel_ID

# Create your models here.
