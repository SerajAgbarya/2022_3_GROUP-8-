from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ScholarshipRequest(models.Model):
    DEGREE_YEAR_CHOICES = [(i, str(i)) for i in range(1, 5)]
    FINANCIAL_SITUATION_CHOICES = [('bad', 'Bad'), ('mid', 'Mid'), ('good', 'Good')]
    YES_NO_CHOICES = [('yes', 'Yes'), ('no', 'No')]

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    degree_year = models.PositiveSmallIntegerField(choices=DEGREE_YEAR_CHOICES)
    age = models.PositiveSmallIntegerField()
    financial_situation = models.CharField(max_length=4, choices=FINANCIAL_SITUATION_CHOICES)
    parent_work = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    special_needs = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    tenant = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    volunteer = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
