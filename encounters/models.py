from django.db import models

from creatures.models import Creature

class Encounters(models.Model):
    title = models.CharField(max_length=50)