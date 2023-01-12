from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from app.constants import NO_YES_CHOICES, FINANCIAL_SITUATION_CHOICES, DEGREE_YEAR_CHOICES


class ScholarshipRequest(models.Model):
    PENDING = 'PENDING'
    UNDER_REVIEW = 'UNDER_REVIEW'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    STATUS_CHOICES = [
        (PENDING, 'Waiting For Review'),
        (UNDER_REVIEW, 'Under Review'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    degree_year = models.PositiveSmallIntegerField(choices=DEGREE_YEAR_CHOICES)
    age = models.PositiveSmallIntegerField()
    financial_situation = models.CharField(max_length=4, choices=FINANCIAL_SITUATION_CHOICES)
    parent_work = models.CharField(max_length=3, choices=NO_YES_CHOICES)
    special_needs = models.CharField(max_length=3, choices=NO_YES_CHOICES)
    tenant = models.CharField(max_length=3, choices=NO_YES_CHOICES)
    volunteer = models.CharField(max_length=3, choices=NO_YES_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    points = models.IntegerField(default=0)


class Task(models.Model):
    TO_DO = 'TO_DO'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    STATUS_CHOICES = [
        (TO_DO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasks_created')
    worker_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasks_assigned')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TO_DO)
    place = models.CharField(max_length=50)
    total_hours = models.PositiveIntegerField()
    completed_hours = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class VolunteerHours(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='hours_added')
    task_id = models.ForeignKey('app.Task', on_delete=models.CASCADE, related_name='task_in_progress')
    date = models.DateField()
    hours = models.IntegerField()


class PointsByYear(models.Model):
    degree_year = models.PositiveSmallIntegerField(choices=DEGREE_YEAR_CHOICES)
    points = models.IntegerField(default=0)


class PointsByAge(models.Model):
    age = models.PositiveSmallIntegerField()
    points = models.IntegerField(default=0)


class PointsByAge(models.Model):
    minAge = models.PositiveSmallIntegerField()
    maxAge = models.PositiveSmallIntegerField()
    points = models.IntegerField(default=0)


class PointsByFinancialSituation(models.Model):
    financial_situation = models.CharField(max_length=4, choices=FINANCIAL_SITUATION_CHOICES)
    points = models.IntegerField(default=0)


class PointsByParentWork(models.Model):
    parent_work = models.CharField(max_length=3, choices=NO_YES_CHOICES)
    points = models.IntegerField(default=0)


class PointsBySpecialNeeds(models.Model):
    special_needs = models.CharField(max_length=3, choices=NO_YES_CHOICES)
    points = models.IntegerField(default=0)


class PointsByTenant(models.Model):
    tenant = models.CharField(max_length=3, choices=NO_YES_CHOICES)
    points = models.IntegerField(default=0)


class PointsByTenant(models.Model):
    tenant = models.CharField(max_length=3, choices=NO_YES_CHOICES)
    points = models.IntegerField(default=0)
