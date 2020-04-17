from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from creatures.models import Creature
from encounters.models import Encounters
from encounters.utils import hydrateEncounter
from user.models import DnDUser

from api.serialize import CreatureSerializer, EncountersSerializer, UserSerializer

class CreatureViewSet(viewsets.ModelViewSet):
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer

    def perform_create(self, serializer):
        if serializer and serializer.validated_data.get("hp"):
            max_hp = serializer.validated_data["hp"]
        serializer.save(max_hp=max_hp)

class EncountersViewSet(viewsets.ModelViewSet):
    queryset = Encounters.objects.all()
    serializer_class = EncountersSerializer

    def retrieve(self, request, pk=None):
        encounter = None

        try:
            encounter = hydrateEncounter(Encounters.objects.get(pk=pk))
        except Exception as e:
            return Response({'error': f'{e}'})

        return Response(encounter)
    
    def list(self, request):
        encounters = None
        try:
            encounters = [hydrateEncounter(e) for e in Encounters.objects.all()]
        except Exception as e:
            return Response({'error': e})
        
        return Response(encounters)

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