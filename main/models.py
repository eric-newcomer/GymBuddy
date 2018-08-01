from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(max_length=2, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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

