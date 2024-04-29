from django import forms
from .models import Bin


# ModelForm for Bin
class BinForm(forms.ModelForm):
    
    class Meta: # Metadaten
        model = Bin 
        exclude = ["color"] # Exclude color from form, as it is set automatically


# Not a ModelForm due to different data type between input and database
class MeasurementForm(forms.Form):

    # Input is stored as a string separated by spaces, 
    # to avoid manually entering all measurements one by one
    Ergebnisse = forms.CharField(max_length=2000)

    # Dropdown menu for all available bins
    Mülleimer = forms.ModelChoiceField(queryset=Bin.objects.all()) 

    # Date and time for the measurement
    StartDatum = forms.DateField()
    Startzeit = forms.TimeField()
