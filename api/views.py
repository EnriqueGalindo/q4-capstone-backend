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
    
    # First we grag the encounter title from the request,
    # Then we grab the creature information from the encounter 
    # and create a new creature in the database for each one of them
    # Then we create the encounter and add that list as the creatures
    def create(self, request):
        title = request.data['title']
        creatures = []

        encounter = Encounters.objects.create(
            title=title,
            description='',
        )

        for creature in request.data['creatures']:
            for _ in range(int(creature['quantity'])):
                newCreature = Creature.objects.create(
                    name=creature['name'],
                    hp=creature['hp'],
                    ac=creature['ac'],
                    status='',
                    secondary_status='',
                    tertiary_status='',
                )

                newCreature.save()
                encounter.creatures.add(newCreature)
        
        encounter.save()

        return Response(hydrateEncounter(encounter))
    
    # We need to figure out which creatures already exist and update them
    # otherwise we create the creatures that were added then add them to
    # the encounter
    def update(self, request, pk=None):
        creatures = request.data['creatures']
        encounter = None

        try:
            encounter = Encounters.objects.get(pk=pk)
            encounter.title = request.data['title']
            for creature in creatures:
                if 'id' in creature:
                    for id in creature['id']:
                        modified_creature = Creature.objects.get(id=id)
                        modified_creature.name = creature['name']
                        modified_creature.hp = creature['hp']
                        modified_creature.ap = creature['ac']
                        modified_creature.status = creature['status'] or ''
                        modified_creature.secondary_status = creature['secondary_status'] or ''
                        modified_creature.tertiary_status = creature['tertiary_status'] or ''
                        modified_creature.consious = creature['conscious']
                        modified_creature.save()
                else:
                    for _ in range(int(creature['quantity'])):
                        new_monster = Creature.objects.create(
                            name=creature['name'],
                            hp=creature['hp'],
                            ac=creature['ac'],
                            status='',
                            secondary_status='',
                            tertiary_status='',
                            conscious=True,
                        )
                        new_monster.save()
                        encounter.creatures.add(new_monster)

            encounter.save()

        except Exception as e:
            print(e)
            return Response({'error': f'{e}'})

        return Response(hydrateEncounter(encounter))
    
    def destroy(self, request, pk=None):
        try:
            encounter = Encounters.objects.get(pk=pk)
            encounter.creatures.all().delete()
            encounter.delete()
        except Exception as e:
            print(e)
            return Response({'error': f'{e}'})
        
        return Response({'deleted': pk})

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