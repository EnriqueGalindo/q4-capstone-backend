from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from creatures.models import Creature
from encounters.models import Encounters
from user.models import DnDUser

from api.serialize import CreatureSerializer, EncountersSerializer, UserSerializer

class CreatureViewSet(viewsets.ModelViewSet):
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer
    def perform_create(self, serializer):
        if serializer and serializer.validated_data.get('hp'):
            max_hp = serializer.validated_data['hp']
        serializer.save(max_hp=max_hp)

class EncountersViewSet(viewsets.ModelViewSet):
    queryset = Encounters.objects.all()
    serializer_class = EncountersSerializer

    @action(detail=True, methods=['get'])
    def reset_encounter(self, request, pk=None):
        encounter = self.get_object()
        for creature in encounter.creatures.all():
            creature.hp = creature.max_hp
            creature.status = ""
            creature.secondary_status = ""
            creature.tertiary_status = ""
            creature.conscious = True
            creature.save()

        return Response({'status': 'creatures reset'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = DnDUser.objects.all()
    serializer_class = UserSerializer

