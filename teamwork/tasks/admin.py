from django.contrib import admin

from teamwork.tasks.models import Files, Tasks
# Register your models here.

admin.site.register(Files)
admin.site.register(Tasks)