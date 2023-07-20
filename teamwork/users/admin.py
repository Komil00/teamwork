from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from teamwork.users.models import Employee, Employer


User = get_user_model()

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("phone", "password", 'type')}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["phone", "name", "is_superuser"]
    search_fields = ["name"]

    def save_model(self, request, obj, form, change):
        if len(str(obj.password)) < 20:
            obj.set_password(obj.password)
        super(UserAdmin, self).save_model(request, obj, form, change)


admin.site.register(Employee)
admin.site.register(Employer)