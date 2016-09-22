from rii_Api.models import Game, Year, Player, Location, Opponent, Coach, Manager
from rest_framework import serializers
from django.contrib.auth.models import User # RT added w createsuperuser - do I still need
from django.views.decorators.csrf import csrf_exempt #RT csrf crashed until I added



class GameSerializer(serializers.HyperlinkedModelSerializer):
    # opponentId = OpponentSerializer()
    class Meta:
        model = Game
        fields = ('id', 'url', 'attendance', 'week', 'result', 'rockIslandScore', 'opponentScore', 'rii1st', 'rii2nd', 'rii3rd', 'rii4th', 'opp1st', 'opp2nd', 'opp3rd', 'opp4th', 'gameSummary', 'yearId', 'opponentId', 'locationId', 'date')

class OpponentSerializer(serializers.HyperlinkedModelSerializer):
    games = GameSerializer(many=True) # makes game an object on opponents # skip to edit or add teams
    class Meta:
        model = Opponent
        fields = ('id', 'url', 'name', 'games')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'url', 'city', 'state', 'venueName', 'games')

class GameSerializer(serializers.HyperlinkedModelSerializer): #added again to get Opponent to show on Seasons
    opponentId = OpponentSerializer() #turn on!
    locationId = LocationSerializer() #turn on! try so can bring in location to game summary
    class Meta:
        model = Game
        fields = ('id', 'url', 'attendance', 'week', 'result', 'rockIslandScore', 'opponentScore', 'rii1st', 'rii2nd', 'rii3rd', 'rii4th', 'opp1st', 'opp2nd', 'opp3rd', 'opp4th', 'gameSummary', 'yearId', 'opponentId', 'locationId', 'date')


class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = ('id', 'url', 'firstName', 'lastName')

class YearSerializer(serializers.HyperlinkedModelSerializer):
    coachId = CoachSerializer() # turn on!need to allow coach to show on yearView
    class Meta:
        model = Year
        fields = ('id', 'url', 'year', 'wins', 'losses', 'ties', 'yearSummary', 'managerId', 'coachId', 'image')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    # season = YearSerializer(many=True)
    class Meta:
        model = Player
        fields = ('id', 'url', 'season', 'nickName', 'firstName', 'lastName', 'legalName', 'position', 'height', 'weight', 'birthDate', 'birthCity', 'birthState', 'birthCountry', 'college', 'playerBio', 'image', 'imageInfo')


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'url', 'firstName', 'lastName')

#Need for superuser Auth
@csrf_exempt
def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Use the built-in authenticate method to verify
    authenticated_user = authenticate(
            username=req_body['username'],
            password=req_body['password']
            )

    # If authentication was successful, log the user in
    success = True
    if authenticated_user is not None:
        login(request=request, user=authenticated_user)
    else:
        success = False

    data = json.dumps({"success":success})
    return HttpResponse(data, content_type='application/json')
