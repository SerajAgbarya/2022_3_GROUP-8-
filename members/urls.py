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
    path('admin_view_student',views.admin_view_student, name='admin_view_student'),
    path('delete_student',views.delete_student, name='delete_student'),
    path('work_hours_list', views.work_hours_list, name='work_hours_list'),
    path('add_work_hours', views.add_work_hours, name='add_work_hours'),

]