from django.shortcuts import render
from rest_framework import viewsets

from creatures.models import Creature
from encounters.models import Encounters
from user.models import DnDUser

from api.serialize import CreatureSerializer, EncountersSerializer, UserSerializer

class CreatureViewSet(viewsets.ModelViewSet):
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer

class EncountersViewSet(viewsets.ModelViewSet):
    queryset = Encounters.objects.all()
    serializer_class = EncountersSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = DnDUser.objects.all()
    serializer_class = UserSerializer