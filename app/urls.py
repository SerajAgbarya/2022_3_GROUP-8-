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
    path('scholarship/submit/', views.submit_scholarship, name='submit_scholarship'),
    path('scholarship/', views.scholarship_form, name='scholarship_form'),
    path('scholarship/view/', views.scholarship_view, name='scholarship_view'),
    path('student/home/', views.student_home_page, name='student_home_page'),
    path('student/volunteer/', views.student_volunteer, name='student_volunteer'),
    path('student/task/', views.student_task, name='student_task'),

]