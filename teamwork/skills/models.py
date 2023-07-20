from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Specialties(MPTTModel):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.name_uz


class Skills(models.Model):
    special = models.ManyToManyField(Specialties, related_name="special_skills", blank=True)
    name = models.CharField(max_length=100)
    is_moderated = models.BooleanField(default=False)

    def __str__(self):
        return self.name