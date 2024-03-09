from django.db import models

# Create your models here.

class Bin(models.Model):

    # Fields of database table
    id = models.AutoField(primary_key = True)
    hasSensor = models.BooleanField(default = False)
    lat = models.FloatField(default = 0.0)
    lon = models.FloatField(default = 0.0)

    def __str__(self):
        return f"Mülleimer: {self.id}"
    
class Measurement(models.Model):

    # Fields of database table
    id = models.AutoField(primary_key = True)
    bin = models.ForeignKey(Bin, on_delete = models.CASCADE)
    value = models.FloatField(default = 0.0)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Messung: {self.id}"