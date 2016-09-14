from rii_Api.models import Game, Year, Player, Location, Opponent, Coach, Manager
from rest_framework import serializers
from django.contrib.auth.models import User # added w createsuperuser


#added - superuser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'password')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'url', 'attendance', 'week', 'result', 'rockIslandScore', 'opponentScore', 'rii1st', 'rii2nd', 'rii3rd', 'rii4th', 'opp1st', 'opp2nd', 'opp3rd', 'opp4th', 'gameSummary', 'yearId', 'opponentId', 'locationId', 'date')


class YearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Year
        fields = ('id', 'url', 'year', 'wins', 'losses', 'ties', 'yearSummary', 'managerId', 'coachId', 'image') #add image


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'url', 'season', 'nickName', 'firstName', 'lastName', 'legalName', 'position', 'height', 'weight', 'birthDate', 'birthCity', 'birthState', 'birthCountry', 'college', 'playerBio', 'image')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'url', 'city', 'state', 'venueName', 'games')

class OpponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opponent
        fields = ('id', 'url', 'name', 'games')

class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = ('id', 'url', 'firstName', 'lastName')

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'url', 'firstName', 'lastName')
