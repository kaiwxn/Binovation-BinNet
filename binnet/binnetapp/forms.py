from django.forms import ModelForm

from .models import Bin, Measurement


class BinForm(ModelForm):
    
    class Meta: # Metadaten
        model = Bin 
        fields = "__all__"


class MeasurementForm(ModelForm):

    class Meta: 
        model = Measurement
        fields = "__all__"