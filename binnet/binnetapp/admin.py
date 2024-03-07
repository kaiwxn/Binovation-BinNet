from django.contrib import admin

# Register your models here.
from binnetapp.models import Mülleimer, Messung

admin.site.register(Mülleimer)
admin.site.register(Messung)