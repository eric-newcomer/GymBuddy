from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    activity1 = models.CharField(max_length=50, blank=True)
    activity2 = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
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

