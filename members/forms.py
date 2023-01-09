from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Hour


class WorkerUserForm(forms.ModelForm):
    """PatientUserForm """
    class Meta:
        """Meta """
        def pub1(self):
            """pub1 """


        def pub2(self):
            """pub2 """

        model = User
        fields = ['first_name', 'last_name', 'username', 'password','email']
        widgets = {
            'password': forms.PasswordInput()
        }



class WorkerForm(forms.ModelForm):
    """PatientForm """
    class Meta:
        """Meta """
        def pub1(self):
            """pub1 """


        def pub2(self):
            """pub2 """

        model = models.Worker
        fields = ['idNumber', 'gender','years', 'age']


class HourForm(forms.ModelForm):
    class Meta:
        model = Hour
        fields = ['date', 'hours', 'task']