from anion.contrib import admin

from ..models import Degree, Discipline, Domain

__all__ = [
    "DegreeAdmin",
    "DisciplineAdmin",
    "DomainAdmin",
]


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    """
    Admin options for the `evaluation.Degree` model.
    """


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    """
    Admin options for the `evaluation.Domain` model.
    """


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    """
    Admin options for the `evaluation.Discipline` model.
    """
