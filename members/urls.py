from django.urls import path
from . import views
# 127.0.0.1:8000/members
urlpatterns = [
    path('', views.index, name='index'),
    path('login_user',views.login_user,name='login_user' ),
    path('worker_login',views.worker_login,name='worker_login' ),
    path('logout_user',views.logout_user,name='logout_user'),
    path('worker_logout',views.logout_worker,name='worker_logout'),

]