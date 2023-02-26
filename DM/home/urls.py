from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
   
]
