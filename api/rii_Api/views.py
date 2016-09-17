from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rii_Api.models import Game, Year, Player, Location, Opponent, Coach, Manager
from rii_Api.serializers import GameSerializer, YearSerializer, PlayerSerializer, LocationSerializer, OpponentSerializer, CoachSerializer, ManagerSerializer
from django.contrib.auth.models import User #added with createsuperuser



class GameList(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class YearList(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer

class PlayerList(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class LocationList(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class OpponentList(viewsets.ModelViewSet):
    queryset = Opponent.objects.all()
    serializer_class = OpponentSerializer

class CoachList(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

class ManagerList(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
