from django.forms import ModelForm
from .models import Squirrel

Class squirrelForm(ModelForm):
    class Meta:
        model = squirrel
        fields = ['Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age']

    # Latitude=forms.FloatField()



# Latitude = models.FloatField(
#     help_text=_('measure in North and South')
# )
#
# Longitude = models.FloatField(
#     help_text=_('measure in East and West')
# )
#
# Unique_Squirrel_ID = models.CharField(
#     max_length=20,
#     help_text=_('unique squirrel id with location, date and time')
# )
#
# AM = 'AM'
# PM = 'PM'
#
# SHIFT_CHOICE = [
#     (AM, _('AM')),
#     (PM, _('PM')),
# ]
#
# Shift = models.CharField(
#     max_length=2,
#     help_text=_('morning or afternoon when sighted'),
#     choices=SHIFT_CHOICE,
# )
#
# Date = models.DateField(
#     help_text=_('pass in date object')
# )
#
# ADULT = 'Adult'
# JUVENILE = 'Juvenile'
#
# AGE_CHOICE = [
#     (ADULT, _('Adult')),
#     (JUVENILE, _('Juvenile')),
# ]
#
# Age = models.CharField(
#     max_length=15,
#     help_text=_('Age of the squirrel'),
#     choices=AGE_CHOICE,
#     null=True,
#     blank=True,
# )
