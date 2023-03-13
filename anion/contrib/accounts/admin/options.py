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


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin options for the `accounts.User` model.
    """
