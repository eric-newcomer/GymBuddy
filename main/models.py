from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gym(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    weights = False
    cardio = False
    powerlifting_friendly = False

    def __str__(self):
        return self.name

class Post(models.Model):
    name = str(User.first_name) + str(User.last_name)
    #date = models.DateTimeField()
    muscles_trained = models.CharField(max_length=50)
    gym_buddy = False
    gym = Gym.name
    image = None

    def __str__(self):
        return self.name

