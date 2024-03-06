from django.forms import ModelForm

from .models import Mülleimer


class MülleimerForm(ModelForm):
    
    class Meta: # Metadaten
        model = Mülleimer 
        fields = "__all__"

