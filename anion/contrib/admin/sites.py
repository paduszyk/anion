from functools import partial

from django.contrib import admin

from .forms import AdminAuthenticationForm

__all__ = [
    "AdminSite",
    "register",
    "site",
]


class AdminSite(admin.AdminSite):
    """
    Base class for the default admin site of the project.
    """

    login_form = AdminAuthenticationForm


# Default admin site instance
site = AdminSite()

# Decorator for registering the models to the default admin site
register = partial(admin.register, site=site)
