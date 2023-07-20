# Generated by Django 4.0.8 on 2022-12-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
        ('users', '0005_employee_skills_employee_specialty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='skills',
            field=models.ManyToManyField(related_name='employee_skills', to='skills.skills'),
        ),
    ]
