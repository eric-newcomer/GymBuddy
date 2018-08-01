from django.contrib import admin
from .models import Post, Gym, Profile
# Register your models here.

admin.site.register(Post)
admin.site.register(Gym)
admin.site.register(Profile)