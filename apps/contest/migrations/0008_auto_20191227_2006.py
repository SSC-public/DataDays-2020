# Generated by Django 2.2.8 on 2019-12-27 20:06

import apps.contest.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0007_auto_20191227_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsubmission',
            name='file_answer',
            field=models.FileField(blank=True, null=True, upload_to=apps.contest.models.QuestionSubmission.upload_path),
        ),
        migrations.AddField(
            model_name='task',
            name='scoring_type',
            field=models.CharField(choices=[('final_trial', 'final_trial'), ('weighted_average', 'weighted_average')], default='weighted_average', max_length=10),
        ),
    ]