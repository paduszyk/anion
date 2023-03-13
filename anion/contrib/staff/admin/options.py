from anion.contrib import admin

from ..models import Contract, Group, Person, Position, Status

__all__ = [
    "ContractAdmin",
    "GroupAdmin",
    "PersonAdmin",
    "PositionAdmin",
    "StatusAdmin",
]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """
    Admin options for the `staff.Person` model.
    """


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """
    Admin options for the `staff.Group` model.
    """


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """
    Admin options for the `staff.Position` model.
    """


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """
    Admin options for the `staff.Status` model.
    """


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """
    Admin options for the `staff.Contract` model.
    """
