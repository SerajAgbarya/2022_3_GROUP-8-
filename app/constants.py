# groups
WORKER = 'WORKER'
STUDENT = 'STUDENT'
MANAGER = 'MANGER'

BAD_SMALL = 'bad'
MID_SMALL = 'mid'
GOOD_SMALL = 'good'
GOOD = 'Good'
MID = 'Mid'
BAD = 'Bad'
ON_SMALL = 'on'
YES_SMALL = 'yes'
NO_SMALL = 'no'
ON = 'On'
YES = 'Yes'
NO = 'No'

STUDENT_LOGIN_PAGE_PATH = '/student/signin/'
STUDENT_HOME_PAGE = '/student/'
STUDENT_PERSONAL_INFO_PAGE = '/student/personal_info/'
NO_YES_CHOICES = [(NO_SMALL, NO), (YES_SMALL, YES)]
FINANCIAL_SITUATION_CHOICES = [(BAD_SMALL, BAD), (MID_SMALL, MID), (GOOD_SMALL, GOOD)]
DEGREE_YEAR_CHOICES = [(i, str(i)) for i in range(1, 5)]
