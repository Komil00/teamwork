# Generated by Django 4.0.8 on 2023-07-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_user_first_name_user_last_name_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of User'),
        ),
    ]
