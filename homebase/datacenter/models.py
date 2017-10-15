from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Location(models.Model):
    KIND_PERSON = 'person'
    KIND_OBJECT = 'object'
    KIND_OTHER = 'other'

    KIND_CHOICES = (
        (KIND_PERSON, 'person'),
        (KIND_OBJECT, 'object'),
        (KIND_OTHER, 'other'),
    )
    latitude = models.CharField(max_length=20, null=True)
    longitude = models.CharField(max_length=20, null=True)
    timestamp = models.DateTimeField('date',default=datetime.now)
    username = models.CharField(max_length=40)
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    kind = models.CharField(max_length=30, choices=KIND_CHOICES, default=KIND_PERSON)
    url = models.URLField(max_length=255, default='',blank=True)
    visible = models.IntegerField(default=1)

    def __str__(self):
        return self.title

