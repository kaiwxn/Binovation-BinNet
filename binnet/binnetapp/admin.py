from django.contrib import admin

# Register your models here.
from binnetapp.models import Bin, Measurement, Ranking

admin.site.register(Bin)
admin.site.register(Measurement)
admin.site.register(Ranking)