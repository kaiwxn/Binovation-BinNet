from django import forms

from .models import Bin


class BinForm(forms.ModelForm):
    
    class Meta: # Metadaten
        model = Bin 
        fields = "__all__"


# Not a ModelForm due to different data type
class MeasurementForm(forms.Form):

    values = forms.CharField(max_length=500)
    bin = forms.ModelChoiceField(queryset=Bin.objects.all()) # Dropdown
