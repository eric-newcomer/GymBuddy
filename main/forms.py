from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Workout
import datetime


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False, help_text="Username:")
    first_name = forms.CharField(max_length=30, required=False, help_text="First name:")
    last_name = forms.CharField(max_length=30, required=False, help_text="Last name:") 
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(max_length=500, required=False, help_text="Bio:", widget=forms.Textarea)
    location = forms.CharField(max_length=30, required=False, help_text="Location:")
    activity1 = forms.CharField(max_length=50, required = False, help_text="Favorite Gym Activity:")
    activity2 = forms.CharField(max_length=50, required = False, help_text="Secondary Favorite Activity:")
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'activity1', 'activity2', 'image')

class WorkoutForm(forms.ModelForm):
    what = forms.CharField(max_length=100, required=False, help_text='What are you training?')
    gym = forms.CharField(max_length=100, required=False, help_text='Where?')

    class Meta:
        model = Workout
        fields = ('what', 'gym')