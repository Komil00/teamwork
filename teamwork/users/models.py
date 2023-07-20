from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from teamwork.skills.models import Specialties, Skills


User_Type = (
    ("EMPLOYEE", "EMPLOYEE"),
    ("EMPLOYER", "EMPLOYER"),

)

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    name = models.CharField(_("Name of User"), max_length=255)
    phone = models.CharField(_("Phone"), unique=True, max_length=13)
    type = models.CharField(max_length=15, choices=User_Type, default=User_Type[0])
    image = models.ImageField(_("Image"), upload_to='user_image', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"phone": self.phone})

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialties, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills, related_name='employee_skills')
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    job_address = models.CharField(max_length=100)

    # Other Info
    passport = models.CharField(max_length=9, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    jins = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    additional_phone = models.CharField(max_length=20, null=True, blank=True)
    language = models.CharField(max_length=20, null=True, blank=True)
    passport = models.CharField(max_length=10, null=True, blank=True)
    pass_by_whom = models.CharField(max_length=100, null=True, blank=True)
    pass_when = models.DateField(null=True, blank=True)
    validity_period = models.DateField(null=True, blank=True)
    passport_copy = models.FileField(upload_to='files/pasport', null=True, blank=True)
    hourly_wage = models.FloatField(default=0, null=True, blank=True)
    site = models.URLField(max_length=100, null=True, blank=True)
    your_description = models.TextField(null=True, blank=True)

    # Social media
    instagram = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.user.phone + ' ' + self.user.name


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organazation_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    employee_count = models.IntegerField()

    # Other info
    fish = models.CharField(max_length=100, null=True, blank=True)
    organization_name = models.CharField(max_length=100, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=20, null=True, blank=True)
    mfo = models.CharField(max_length=20, null=True, blank=True)
    inn = models.CharField(max_length=50, null=True, blank=True)
    ifut = models.CharField(max_length=50, null=True, blank=True)
    legal_address = models.CharField(max_length=100, null=True, blank=True)
    index = models.CharField(max_length=20, null=True, blank=True)
    telegram_phone = models.CharField(max_length=20, null=True, blank=True)
    site = models.URLField(max_length=100, null=True, blank=True)
    
    # Social media
    instagram = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.phone + ' ' + self.user.name
