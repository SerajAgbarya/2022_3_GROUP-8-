from django.urls import path
from . import views

# 127.0.0.1:8000/members
urlpatterns = [
    path('', views.index, name='index'),
    path('manager_home', views.index, name='index'),
    path('login_user',views.login_user,name='login_user' ),
    path('worker_login',views.worker_login,name='worker_login' ),
    path('logout_user',views.logout_user,name='logout_user'),
    path('worker_logout',views.logout_worker,name='worker_logout'),
    path('logout_user',views.logout_user,name='logout'),
    path('worker_list', views.worker_list, name='Worker_list'),
    path('transfer_to_worker', views.transfer_to_worker, name='transfer_to_worker'),
    path('delete_worker', views.delete_worker, name='delete_worker'),
    path('worker_details', views.worker_details, name='worker_details'),
    path('money_request', views.money_request, name='money_request'),
    path('student_list',views.student_list, name='student_list'),
    path('delete_student',views.delete_student, name='delete_student'),
    path('add_workhours', views.add_workhours, name='add_workhours'),
    path('view_workhours', views.view_workhours, name='view_workhours'),
    path('delete_workhours/<int:pk>/', views.delete_workhours, name='delete_workhours'),
    path('home_pageworker', views.home_pageworker, name='home_pageworker'),
    path('worker_tasks', views.worker_tasks, name='worker_tasks'),
    path('accept_scholarship', views.scholarship_requests, name='accept_scholarship'),


]