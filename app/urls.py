from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('manager-signin', views.manager_signin, name='manager_signin'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('student-signup', views.student_signup, name='student_signup'),
    path('student-signin', views.manager_signin, name='student_signin'),

]