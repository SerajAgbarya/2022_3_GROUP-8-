from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ScholarshipRequest(models.Model):
    DEGREE_YEAR_CHOICES = [(i, str(i)) for i in range(1, 5)]
    FINANCIAL_SITUATION_CHOICES = [('bad', 'Bad'), ('mid', 'Mid'), ('good', 'Good')]
    YES_NO_CHOICES = [('yes', 'Yes'), ('no', 'No')]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    degree_year = models.PositiveSmallIntegerField(choices=DEGREE_YEAR_CHOICES)
    age = models.PositiveSmallIntegerField()
    financial_situation = models.CharField(max_length=4, choices=FINANCIAL_SITUATION_CHOICES)
    parent_work = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    special_needs = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    tenant = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    volunteer = models.CharField(max_length=3, choices=YES_NO_CHOICES)
