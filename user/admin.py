from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


# Register your models here.
class UserConfig(UserAdmin):
    model = User
    search_fields = ['id', 'email', 'first_name', 'last_name']
    list_display = ['id', 'email', 'first_name', 'last_name']
    list_display_links = ['id', 'email']
    ordering = []
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "created_at",
                    "updated_at",
                ],
            },
        ),
    ]
    add_fieldsets = (
        (None, {
            "fields": [
                "email",
                "first_name",
                "last_name",
                "is_staff",
                "is_active",
                "is_superuser",
                "created_at",
                "updated_at",
                "password1",
                "password2",
            ], }
         ),
    )
    readonly_fields = ["created_at", "updated_at", "last_login", "username"]


admin.site.register(User, UserConfig)
