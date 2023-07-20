from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from teamwork.skills.models import Specialties
from teamwork.users.models import Employee, Employer

User = get_user_model()


class STATUS(models.IntegerChoices):
    AKTIVE = 1, _('AKTIVE')
    BAJARILMOQDA = 2, _('BAJARILMOQDA')
    BAJARILDI = 3, _('BAJARILDI')


class Files(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/%Y/%m/%d')

    def __str__(self):
        return self.name


class Tasks(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_tasks', on_delete=models.SET_NULL, null=True, blank=True)
    employer = models.ForeignKey(Employer, related_name='employer_tasks', on_delete=models.SET_NULL, null=True, blank=True)
    specialty = models.ForeignKey(Specialties, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.FloatField()
    time = models.DateTimeField()
    file = models.ManyToManyField(Files, related_name='task_files', blank=True)
    status = models.IntegerField(default=STATUS.AKTIVE, choices=STATUS.choices)
    is_active = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title + ' | ' + str(self.amount)

