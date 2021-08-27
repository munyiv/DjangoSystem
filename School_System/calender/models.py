from datetime import datetime
from django.db import models

# Create your models here.
class Calender(models.Model):
    venue=models.CharField(max_length=20,null=True)
    event_id=models.CharField(max_length=20,null=True)
    event_name=models.CharField(max_length=20,null=True)
    event_duration=models.DurationField(null=True)
    event_planner=models.CharField(max_length=20,null=True)
    event_participants=models.TextField(null=True)
    start_time=models.DateTimeField(null=True)
    end_time=models.DateTimeField(null=True)
    

