from django.urls import path

from members import views as v1
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
    # student urls
    path('student/', views.student_home_page, name='student_home_page'),
    path('student/scholarship/submit/', views.submit_scholarship, name='submit_scholarship'),
    path('student/scholarship/create/', views.scholarship_form, name='scholarship_form'),
    path('student/scholarship/', views.scholarship_view, name='scholarship_view'),
    path('student/scholarship/edit/', views.scholarship_view, name='scholarship_view'),  # TODO handle edit
    path('student/task/', views.student_task_page, name='student_task'),

    path('login_user', v1.login_user, name='login_user'),

]
