# Generated by Django 2.2.8 on 2019-12-28 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_resetpasswordtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivateUserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
            ],
        ),
    ]
