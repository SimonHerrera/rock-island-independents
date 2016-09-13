from django.db import models
from django.utils import timezone # do I need this?


year = [(number, number) for number in range(1919, 1926)]
height = [(number, number) for number in range(48, 83)]
result = [('W', 'W'), ('L', 'L'), ('T', 'T'),]



class Coach(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=25)

    def __str__(self):
        return '{0} {1}'.format(self.firstName, self.lastName)

class Manager(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=25)

    def __str__(self):
        # return self.lastName #only showed part of name, now shows all, is that legit?
        return '{0} {1}'.format(self.firstName, self.lastName)

class Opponent(models.Model): # This comes first because mentioned by Game (OpponentId)
    name = models.CharField(max_length=35) #why dont I need a default here?

    def __str__(self): #what are these do I need them? wht name when could be other properties here - will show is tables
        return self.name

class Location(models.Model):
    city = models.CharField(default='Rock Island', max_length=40)
    state = models.CharField(default='IL', max_length=2)
    venueName = models.CharField(default='Douglas Park', max_length=50)

    def __str__(self):
        return self.venueName

class Year(models.Model):
    year = models.IntegerField(choices=year, default=1919)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    yearSummary = models.TextField(default='', max_length=2000)
    managerId = models.ForeignKey(Manager, related_name='years', on_delete=models.SET_NULL, null=True)
    coachId = models.ForeignKey(Coach, related_name='years', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to = 'year_images/', default = 'year_images/default_year_image.jpg')

    def __str__(self):
        return str(self.year)


class Player(models.Model):
    season = models.ManyToManyField(Year) #by default this is a foreign key
    nickName = models.CharField(default='', max_length=25)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=25)
    legalName = models.CharField(max_length=70)
    position = models.CharField(max_length=2)
    height = models.IntegerField(choices=height, default=48)
    weight = models.IntegerField(default=170)
    birthDate = models.DateField(auto_now=False, auto_now_add=False) #need both of these?
    birthCity = models.CharField(default='', max_length=35)
    birthState = models.CharField(default='', max_length=2)
    birthCountry = models.CharField(default='USA', max_length=30)
    college = models.CharField(default='None', max_length=45)
    playerBio = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'player_images/', default = 'player_images/default_player_image.jpg')


    def __str__(self):
        return '{0} {1}'.format(self.firstName, self.lastName)

class Game(models.Model):
    attendance = models.CharField(default='NA', max_length=5) # Could have as Integer and filter as NA on front OR as sting and 1,000 and NA
    week = models.IntegerField(default=0)
    result = models.CharField(choices=result, max_length=1) #makes me add a default - didn't need that on music history, why?
    rockIslandScore = models.IntegerField(default=0)
    opponentScore = models.IntegerField(default=0)
    rii1st = models.IntegerField(default=0)
    rii2nd = models.IntegerField(default=0)
    rii3rd = models.IntegerField(default=0)
    rii4th = models.IntegerField(default=0)
    opp1st = models.IntegerField(default=0)
    opp2nd = models.IntegerField(default=0)
    opp3rd = models.IntegerField(default=0)
    opp4th = models.IntegerField(default=0)
    gameSummary = models.TextField(default='There is no Game summary yet for this game.', max_length=2000) #Use textfield on larger text
    opponentId = models.ForeignKey(Opponent, related_name='games', on_delete=models.SET_NULL, null=True)
    yearId = models.ForeignKey(Year, related_name='games', on_delete=models.SET_NULL, null=True) #maybe need to make foreign key
    locationId = models.ForeignKey(Location, related_name='games', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self): #What is this doing, is unicode right?
        return '{0} {1}'.format(self.week, self.yearId)
