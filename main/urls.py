# not master urls
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('workout/', views.workout, name='workout'),
    path('friends/', views.friends, name='friends'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)