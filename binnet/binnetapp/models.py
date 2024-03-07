from django.db import models

# Create your models here.

class Mülleimer(models.Model):

    id = models.AutoField(primary_key = True)
    hatSensor = models.BooleanField(default = False)
    lat = models.FloatField(default = 0.0)
    lon = models.FloatField(default = 0.0)

    def __str__(self):
        return f"Mülleimer: {self.id}"
    
class Messung(models.Model):
    id = models.AutoField(primary_key = True)
    mülleimer = models.ForeignKey(Mülleimer, on_delete = models.CASCADE)
    value = models.FloatField(default = 0.0)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Messung: {self.id}"