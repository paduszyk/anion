from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsAppConfig(AppConfig):
    """
    Configuration class for the `accounts` app.
    """

    name = "anion.contrib.accounts"
    verbose_name = _("Accounts")
