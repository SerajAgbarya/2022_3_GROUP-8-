# Generated by Django 3.2.7 on 2023-01-11 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230108_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarshiprequest',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scholarshiprequest',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Waiting For Review'), ('UNDER_REVIEW', 'Under Review'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=20),
        ),
    ]
