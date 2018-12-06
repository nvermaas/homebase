from django.db import models
from django.utils.timezone import datetime

class MoonPhases(models.Model):
    phase = models.CharField(max_length=15)
    timestamp = models.DateTimeField('date',default=datetime.now, null=True)

    def __str__(self):
        return self.phase + " @ " + str(self.timestamp)
