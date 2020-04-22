import json

from django.test import TestCase

from creatures.models import Creature
from .models import Encounters

from .utils import hydrateEncounter

# Create your tests here.
class HydrationTest(TestCase):
    def setUp(self):
        encounter = Encounters.objects.create(
            title='test',
            description='',
        )
        creature = Creature.objects.create(
            name='Goblin',
            hp=100,
            max_hp=100,
            ac=100,
        )

    def test_hydration(self):
        encounter = Encounters.objects.get(title='test')
        creature = Creature.objects.get(name='Goblin')
        encounter.creatures.add(creature)

        expected_creatures = json.dumps([{
            "id": 1,
            "name": "Goblin",
            "hp": 100,
            "max_hp": 100,
            "ac": 100,
            "status": "",
            "secondary_status": "",
            "tertiary_status": "",
            "conscious": True
        }])

        encounter = hydrateEncounter(encounter)
        actual_creatures = json.dumps(encounter['creatures'])

        self.assertEqual(expected_creatures, actual_creatures)
