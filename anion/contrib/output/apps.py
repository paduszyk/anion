from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OutputAppConfig(AppConfig):
    """
    Configuration class for the `output` app.
    """

    name = "anion.contrib.output"
    verbose_name = _("Output")
