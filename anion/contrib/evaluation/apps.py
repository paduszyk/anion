from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EvaluationAppConfig(AppConfig):
    """
    Configuration class for the `evaluation` app.
    """

    name = "anion.contrib.evaluation"
    verbose_name = _("Evaluation")
