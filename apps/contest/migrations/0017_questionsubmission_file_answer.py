# Generated by Django 2.2.8 on 2020-01-10 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0016_remove_questionsubmission_file_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsubmission',
            name='file_answer',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]