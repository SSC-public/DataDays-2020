# Generated by Django 2.2.8 on 2019-12-18 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='education',
        ),
    ]
