from django.db import models

# Create your models here.

class Mülleimer(models.Model):

    id = models.AutoField(primary_key=True)
    hatSensor = models.BooleanField(default=False)
    standort = models.CharField(max_length=100)

    def __int__(self):
        return self.id