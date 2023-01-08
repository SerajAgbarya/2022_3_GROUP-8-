# Generated by Django 3.2.2 on 2023-01-08 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNumber', models.CharField(max_length=9)),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')])),
                ('age', models.IntegerField(default=15)),
                ('email', models.CharField(max_length=100)),
                ('years', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Members',
        ),
    ]
