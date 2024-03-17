from django import forms
from .models import Bin


# ModelForm for Bin
class BinForm(forms.ModelForm):
    
    class Meta: # Metadaten
        model = Bin 
        fields = "__all__"


# Not a ModelForm due to different data type between input and database
class MeasurementForm(forms.Form):

    # Input is stored as a string separated by spaces, 
    # to avoid manually entering all measurements one by one
    values = forms.CharField(max_length=500)

    # Dropdown menu for all available bins
    bin = forms.ModelChoiceField(queryset=Bin.objects.all()) 

    # Date and time for the measurement
    startingDate = forms.DateField()
    startingTime = forms.TimeField()
