from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StaffAppConfig(AppConfig):
    """
    Configuration class for the `staff` app.
    """

    name = "anion.contrib.staff"
    verbose_name = _("Staff")
