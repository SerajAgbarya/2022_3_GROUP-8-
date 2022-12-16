from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('manager-signin', views.manager_signin, name='manager_signin'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('activate-worker/<uidb64>/<token>', views.activate_worker, name='activate_worker'),
    path('student-signup', views.student_signup, name='student_signup'),
    path('student-signin', views.student_signin, name='student_signin'),
    path('worker-signup', views.worker_signup, name='worker_signup'),
    path('worker-signin', views.worker_signin, name='worker_signin'),

]