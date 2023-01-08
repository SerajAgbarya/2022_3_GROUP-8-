# Generated by Django 4.1.4 on 2023-01-07 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarshipRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_year', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('age', models.PositiveSmallIntegerField()),
                ('financial_situation', models.CharField(choices=[('bad', 'Bad'), ('mid', 'Mid'), ('good', 'Good')], max_length=4)),
                ('parent_work', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('special_needs', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('tenant', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('volunteer', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]