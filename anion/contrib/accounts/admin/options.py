from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from anion.contrib import admin

from ..models import Group, User

__all__ = [
    "GroupAdmin",
    "UserAdmin",
]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """
    Admin options for the `accounts.Group` model.
    """

    filter_horizontal = ["permissions"]
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin, UserAdmin):
    """
    Admin options for the `accounts.User` model.
    """

    add_fieldsets = [
        (None, {"fields": ["username", "email", "password1", "password2"]})
    ]
    fieldsets = [
        (_("Status"), {"fields": ["is_active"]}),
        (_("Identifiers"), {"fields": ["username", "email"]}),
        (_("Roles"), {"fields": ["is_staff", "is_superuser"]}),
        (_("Authorization"), {"fields": ["groups", "user_permissions"]}),
        (_("Important dates"), {"fields": ["date_joined", "last_login"]}),
    ]
    filter_horizontal = ["groups", "user_permissions"]
    list_display = [
        "username",
        "email",
        "is_active",
        "last_login",
        "date_joined",
    ]
    list_filter = []
    ordering = ["-date_joined"]
    readonly_fields = ["date_joined", "last_login"]
