from django.db import models

from creatures.models import Creature

class Encounters(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    creatures = models.ManyToManyField(Creature)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title