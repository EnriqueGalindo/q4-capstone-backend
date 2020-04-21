from rest_framework import serializers

from creatures.models import Creature
from encounters.models import Encounters
from user.models import DnDUser

class CreatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creature
        fields = [
            'id',
            'name',
            'hp',
            'ac',
            'status',
            'secondary_status',
            'tertiary_status',
            'conscious'
        ]


class EncountersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Encounters
        fields = [
            'id',
            'title',
            'description',
            'creatures',
            'created_on'
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DnDUser
        fields = [
            'id',
            'username',
            'name',
            'email'
        ]