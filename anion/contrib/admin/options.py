from django.contrib import admin

__all__ = [
    "ModelAdmin",
]


class ModelAdmin(admin.ModelAdmin):
    """
    Base class for all model admin classes defined in the project.
    """
