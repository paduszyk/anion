from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from ..models import Group, User


class GroupAdminChangeForm(forms.ModelForm):
    """
    Form for changing the `accounts.Group` objects in the admin site.
    """

    class Meta:
        model = Group
        exclude = []


class UserAdminChangeForm(forms.ModelForm):
    """
    Form for changing the `accounts.User` objects in the admin site.
    """

    class Meta:
        model = User
        exclude = []


class UserAdminCreationForm(UserCreationForm):
    """
    Form for creating the `accounts.User` objects in the admin site.
    """

    error_messages = {
        "password_mismatch": _(
            "Password confirmation and password do not match."
        )
    }

    def __init__(self, *args, **kwargs):  # pragma: no cover
        super().__init__(*args, **kwargs)
        self.fields["password2"].label = _("Password confirmation")
        self.fields["password2"].help_text = ""
