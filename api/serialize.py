from rest_framework import serializers

from creatures.models import Creature
from encounters.models import Encounters
from user.models import DnDUser

class CreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature
        fields = [
            'id',
            'name',
            'hp',
            'ac',
            'status',
            'conscious'
        ]


class EncountersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encounters
        fields = [
            'id',
            'title',
            'description',
            'creatures',
            'created_on'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DnDUser
        fields = [
            'id',
            'username',
            'name',
            'email'
        ]