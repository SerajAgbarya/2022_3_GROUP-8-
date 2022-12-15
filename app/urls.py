from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.main),
    path("manager-signin/", views.manager_signin)
]