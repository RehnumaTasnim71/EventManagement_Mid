from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    organizer = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='organized_events',
    null=True,  
    blank=True
)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='event_images/', default='default.jpg')
    date = models.DateTimeField()
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='rsvp_events',
        blank=True
    )

    def __str__(self):
        return self.title
