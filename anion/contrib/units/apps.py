from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UnitsAppConfig(AppConfig):
    """
    Configuration class for the `units` app.
    """

    name = "anion.contrib.units"
    verbose_name = _("Units")
