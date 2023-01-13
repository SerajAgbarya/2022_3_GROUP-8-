from django.urls import path

from members import views as v1
from . import views
from .icons import icons
from .scholarship import scholarship
from .signIn import logout
from .tasks import tasks
from .user import user_info
from .volunteer import volunteer_hours

urlpatterns = [
    path('', views.main, name='home'),
    path('manager-signin', views.manager_signin, name='manager_signin'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('activate-worker/<uidb64>/<token>', views.activate_worker, name='activate_worker'),
    path('worker-signup', views.worker_signup, name='worker_signup'),
    path('worker-signin', views.worker_signin, name='worker_signin'),

    # Icons & Images
    path('icons/user-icon.png', icons.get_student_user_icon, name='student_user_icon'),

    # student urls
    path('student/', views.student_home_page, name='student_home_page'),
    path('student/signup/', views.student_signup, name='student_signup'),
    path('student/signin/', views.student_signin, name='student_signin'),
    path('student/logout/', logout.student_logout, name='student_logout'),
    path('student/scholarship/submit/', scholarship.submit_scholarship_reqeust, name='submit_scholarship'),
    path('student/scholarship/create/', scholarship.scholarship_form, name='scholarship_form'),
    path('student/scholarship/', scholarship.scholarship_view, name='scholarship_view'),
    path('student/scholarship/edit/', scholarship.scholarship_view, name='scholarship_view'),  # TODO handle edit
    path('student/task/', tasks.student_task_page, name='student_task'),
    path('student/volunteer/', volunteer_hours.student_volunteer_page, name='student_voulunteer'),
    path('student/volunteer/save/', volunteer_hours.student_save_volunteer, name='student_save_volunteer'),
    path('student/personal_info/', user_info.edit_student_personal_info, name='edit_student_personal_info'),

    path('login_user', v1.login_user, name='login_user'),

]
