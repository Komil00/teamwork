# Generated by Django 4.0.8 on 2023-07-18 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_user_first_name_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
