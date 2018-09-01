from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseNotAllowed
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from .backend import authenticate
from .forms import SignUpForm, ProfileForm, UserForm, WorkoutForm
from.models import Workout
from django.contrib.auth.models import User
from fuzzywuzzy import fuzz


def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(request, username=username,
                                password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        signup_form = SignUpForm()
    return render(request, 'main/signup.html', {
        'signup_form': signup_form,
    })


@login_required
def index(request):
    user_activity = request.user.profile.activity1
    context = {
        'user_activity': user_activity,
    }
    return render(request, 'main/landing.html', context)


class LoginView(View):

    def get(self, request, *args, **kwags):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'main/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(
                request, 'Failed to sign in! Please check your name and PIN', extra_tags='danger')
            return redirect('/login')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')


@login_required
def about(request):
    return render(request, 'main/about.html')


@login_required
def friends(request):
    friend_list = []
    friend_list_2 = []
    current_user = request.user
    users = User.objects.all()
    for user in users:
        if fuzz.ratio(current_user.profile.activity1, user.profile.activity1) > 85 and user != current_user:
            friend_list.append(user)
    for user in users:
        if fuzz.ratio(current_user.profile.activity2, user.profile.activity2) > 85 and user != current_user:
            friend_list_2.append(user)
    context = {
        'friend_list': friend_list,
        'friend_list_2': friend_list_2,
        'current_user': current_user,
    }
    return render(request, 'main/friends.html', context)


@login_required
def profile(request):
    user = request.user
    workouts = Workout.objects.all().order_by('-time')
    context = {
        'user': user,
        'workouts': workouts,
    }
    return render(request, 'main/profile.html', context)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print('Profile successfully updated.')
            return redirect('/profile')
        else:
            print('Error!')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required
def workout(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            print('Workout successfully logged.')
            return redirect('/profile')
        else:
            print("Error!")
    else:
        form = WorkoutForm()
    return render(request, 'main/workout.html', {
        'form': form,
    })
