from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('sign in', views.signup, name="sign in"),
    path('sign out', views.signup, name="sign out"),
    path('sign out2', views.signup, name="sign out2"),
]