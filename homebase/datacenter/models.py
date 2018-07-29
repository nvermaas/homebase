from django.db import models
from django.utils.timezone import datetime

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
    timestamp = models.DateTimeField('date',default=datetime.now, null=True)
    username = models.CharField(max_length=40)
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    kind = models.CharField(max_length=30, choices=KIND_CHOICES, default=KIND_PERSON)
    url = models.URLField(max_length=255, default='',blank=True)
    visible = models.IntegerField(default=1)

    def __str__(self):
        return self.username + " @ " + str(self.timestamp) + " - " + str(self.description)

class Item(models.Model):
    KIND_FOLDER = 'folder'
    KIND_IT_PROJECT = 'IT-project'
    KIND_GALLERY = 'gallery'
    KIND_EXTERNAL_LINK = 'external-link'
    KIND_WIKI = 'wiki'
    KIND_DOCS = 'docs'
    KIND_RESTRICTED = 'restricted'
    KIND_OTHER = 'other'

    KIND_CHOICES = (
        (KIND_IT_PROJECT, 'IT-project'),
        (KIND_GALLERY, 'gallery'),
        (KIND_EXTERNAL_LINK, 'external-link'),
        (KIND_FOLDER, 'folder'),
        (KIND_WIKI, 'wiki'),
        (KIND_DOCS, 'docs'),
        (KIND_RESTRICTED, 'restricted'),
        (KIND_OTHER, 'other'),
    )

    BUTTON_TYPE_CHOICES = (
        ('default', 'default'),
        ('primary', 'primary'),
        ('success', 'success'),
        ('info', 'info'),
        ('warning', 'warning'),
        ('danger', 'danger'),
    )

    key = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    url_image = models.URLField(max_length=255, default='',blank=True)
    url_link  = models.URLField(max_length=255, default='',blank=True)
    url_link_type = models.CharField(max_length=10, choices=BUTTON_TYPE_CHOICES, default='primary')
    url_link_label = models.CharField(max_length=15, default='GO!')
    url_docs = models.URLField(max_length=255, default='', blank=True)
    url_docs_type = models.CharField(max_length=10, choices=BUTTON_TYPE_CHOICES, default='info')
    url_docs_label = models.CharField(max_length=15, default='docs')
    url_wiki = models.URLField(max_length=255, default='', blank=True)
    url_wiki_type = models.CharField(max_length=10, choices=BUTTON_TYPE_CHOICES, default='warning')
    url_wiki_label = models.CharField(max_length=15, default='wiki')

    kind = models.CharField(max_length=30, choices=KIND_CHOICES, default=KIND_OTHER)
    parent = models.CharField(max_length=40,default='',null=True)
    order = models.IntegerField(default=1)
    restricted_to=models.CharField(max_length=255, default='',null=True)

    def __str__(self):
        return self.name