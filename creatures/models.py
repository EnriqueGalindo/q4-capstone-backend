from django.db import models

class Creature(models.Model):

    class CreatureStatus(models.TextChoices):
        BLINDED = 'Blinded'
        CHARMED = 'Charmed'
        DEAFENED = 'Deafened'
        FATIGUED = 'Fatigued'
        FRIGHTENED = 'Frightened'
        GRAPPLED = 'Grappled'
        INCAPACITATED = 'Incapacitated'
        INVISIBLE= 'Invisible'
        PARALYZED = 'Paralyzed'
        PETRIFIED = 'Petrified'
        POISONED = 'Poisoned'
        PRONE = 'Prone'
        RESTRAINED = 'Restrained'
        STUNNED = 'Stunned'

    name = models.CharField(max_length=50)
    hp = models.IntegerField(default=0)
    ac = models.IntegerField(default=0)
    status = models.CharField(max_length=13, choices=CreatureStatus.choices, blank=True)
    secondary_status = models.CharField(max_length=13, choices=CreatureStatus.choices, blank=True)
    tertiary_status = models.CharField(max_length=13, choices=CreatureStatus.choices, blank=True)
    conscious = models.BooleanField(default=True)

    def __str__(self):
        return self.name