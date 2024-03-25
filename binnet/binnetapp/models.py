from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Bin(models.Model):
    
    # Fields of database table
    id = models.AutoField(primary_key = True)
    hasSensor = models.BooleanField(default = False)
    latitude = models.FloatField(default = 0.0, blank = False)
    longitude = models.FloatField(default = 0.0, blank = False)
    
    def __str__(self):
        return f"Mülleimer: {self.id}"
    

class Measurement(models.Model):

    # Fields of database table
    id = models.AutoField(primary_key = True)
    bin = models.ForeignKey(Bin, on_delete = models.CASCADE)
    value = models.FloatField(default = 0.0)
    
    # Date and time of measurement
    measureTime = models.TimeField(default = datetime.time(0, 0, 0)) # 00:00 as default
    measureDate = models.DateField(default = timezone.now()) # Monday as default

    def __str__(self):
        return f"Messung: {self.id}"
    

class Ranking(models.Model):

    # Enumeration for color of bin
    class Color(models.TextChoices):
        RED = "R", "Red"
        ORANGE = "O", "Orange"
        GREEN = "G", "Green"

    id = models.AutoField(primary_key = True)
    bin = models.ForeignKey(Bin, on_delete = models.CASCADE)

    # 1: Monday, 2: Tuesday, ..., 7: Sunday
    weekday = models.IntegerField(default = 0)
    color = models.CharField(max_length = 7, choices = Color, default = Color.GREEN)

    def __str__(self):
        return f"Ranking: {self.id}"