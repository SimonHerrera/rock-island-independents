from django.db import models
from django.utils import timezone

year = [(number, number) for number in range(1907, 1926)]


class Game(models.Model):
    attendance = models.IntegerField(default=0) # can default = NA or a number?

    def __unicode__(self): #What is this doing, is unicode right?
        return self.attendance

class Year(models.Model):
    year = models.IntegerField(choices=year, default=1907)

    def __unicode__(self):
        return self.year

class Player(models.Model):
    position = models.CharField(max_length=2)

    def __str__(self):
        return self.postion

class Location(models.Model):
    # city = models.CharField(max_length=40)
    # state = models.CharField(max_length=20)
    venueName = models.CharField(max_length=25)

    def __str__(self):
        return self.venueName

class Opponent(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Coach(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=15)

    def __str__(self):
        return self.lastName

class Manager(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return self.lastName
