from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
)

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idNumber = models.CharField(max_length=9)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.IntegerField(default=15)
    email = models.CharField(max_length=100)
    years = models.IntegerField(default=1)


class Hour(models.Model):
    date = models.DateField()
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    task = models.CharField(max_length=255)


