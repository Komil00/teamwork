from django.contrib import admin

from teamwork.skills.models import Skills, Specialties
from mptt.admin import DraggableMPTTAdmin
# Register your models here.
admin.site.register(Skills)

@admin.register(Specialties)
class SpecialtiesAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20