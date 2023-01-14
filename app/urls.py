from django.urls import path

from members import views as v1
from . import views
from .services.home import student_main_service
from .services.scholarship import scholarship_services
from .services.signIn import logout_services
from .services.tasks import tasks_services
from .services.user import user_info_services
from .services.volunteer import volunteer_hours_services

urlpatterns = [
    path('', views.main, name='home'),
    path('manager-signin', views.manager_signin, name='manager_signin'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('activate-worker/<uidb64>/<token>', views.activate_worker, name='activate_worker'),
    path('worker-signup', views.worker_signup, name='worker_signup'),
    path('worker-signin', views.worker_signin, name='worker_signin'),

    # student urls
    path('student/', student_main_service.student_home_page, name='student_home_page'),
    path('student/signup/', views.student_signup, name='student_signup'),
    path('student/signin/', views.student_signin, name='student_signin'),
    path('student/logout/', logout_services.student_logout, name='student_logout'),
    path('student/scholarship/submit/', scholarship_services.submit_scholarship_reqeust, name='submit_scholarship'),
    path('student/scholarship/create/', scholarship_services.scholarship_form, name='scholarship_form'),
    path('student/scholarship/', scholarship_services.scholarship_view, name='scholarship_view'),
    path('student/scholarship/edit/', scholarship_services.scholarship_view, name='scholarship_edit'),
    path('student/task/', tasks_services.student_task_page, name='student_task'),
    path('student/volunteer/', volunteer_hours_services.student_volunteer_page, name='student_volunteer'),
    path('student/volunteer/save/', volunteer_hours_services.student_save_volunteer, name='student_save_volunteer'),
    path('student/personal_info/', user_info_services.edit_student_personal_info, name='edit_student_personal_info'),

    path('login_user', v1.login_user, name='login_user'),

]
