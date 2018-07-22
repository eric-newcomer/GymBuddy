from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

def authenticate(request, username=None, password=None):
    for user in User.objects.all().filter(username__iexact=username):
        pwd_valid = check_password(password, user.password)
        if pwd_valid:
            return user
    return None