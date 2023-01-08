from django.urls import path
from . import views
# 127.0.0.1:8000/members
urlpatterns = [
    path('', views.index, name='index'),
    path('manager_home', views.index, name='index'),
    path('login_user',views.login_user,name='login_user' ),
    path('logout_user',views.logout_user,name='logout'),
    path('worker_list', views.worker_list, name='Worker_list'),
    path('transfer_to_worker', views.transfer_to_worker, name='transfer_to_worker'),
    path('delete_worker', views.delete_worker, name='delete_worker'),


]