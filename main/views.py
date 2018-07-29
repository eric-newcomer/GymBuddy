from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseNotAllowed
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from .backend import authenticate
from .forms import SignUpForm



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})

def index(request):
    if request.user.is_authenticated:
        return render(request, 'main/home.html')
    return render(request, 'main/landing.html')

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
def find(request):
   return render(request, 'main/find.html')
