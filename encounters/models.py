from django.db import models
from django.utils import timezone

from creatures.models import Creature

class Encounters(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    creatures = models.ManyToManyField(Creature)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title