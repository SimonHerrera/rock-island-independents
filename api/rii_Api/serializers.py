from rii_Api.models import Game, Year, Player, Location, Opponent, Coach, Manager
from rest_framework import serializers


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'url', 'attendance')


class YearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Year
        fields = ('id', 'url', 'year')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'url', 'position')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'url', 'venueName')

class OpponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opponent
        fields = ('id', 'url', 'name')

class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = ('id', 'url', 'firstName', 'lastName')

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'url', 'firstName', 'lastName')
