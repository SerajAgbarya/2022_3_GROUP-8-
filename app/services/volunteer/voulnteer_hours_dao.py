from app.models import VolunteerHours


def create_new_volunteer_hours(date, hours, task, user):
    if date is None or hours is None or task is None or user is None:
        return
    return VolunteerHours.objects.create(date=date, hours=hours, task_id=task, user_id=user)


def get_volunteer_hours(user):
    if user is None:
        return []
    return VolunteerHours.objects.filter(user_id=user.id)
