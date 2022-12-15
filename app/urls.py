from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.main, name='home'),
    path("manager-signin/", views.manager_signin, name='manager_signin')
]