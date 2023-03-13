from anion.contrib import admin

from ..models import Department, Institute, Institution

__all__ = [
    "DepartmentAdmin",
    "InstituteAdmin",
    "InstitutionAdmin",
]


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    """
    Admin options for the `units.Institution` model.
    """


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    """
    Admin options for the `units.Institute` model.
    """


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """
    Admin options for the `units.Department` model.
    """
