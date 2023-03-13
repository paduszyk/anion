from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class AdminAuthenticationForm(AdminAuthenticationForm):
    """
    Form for authenticating users accessing the admin site.
    """

    error_messages = {
        "invalid_login": _("Invalid login credentials."),
        "unauthorized": _(
            "Only administrators may log in to the administration site."
        ),
        "inactive": _("The account is not active."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the `username` field label to clearly indicate that one can
        # use either username or e-mail address to authenticate.
        opts = UserModel._meta
        self.fields["username"].label = "{} / {}".format(
            capfirst(opts.get_field(UserModel.USERNAME_FIELD).verbose_name),
            opts.get_field(UserModel.EMAIL_FIELD).verbose_name,
        )

    def confirm_login_allowed(self, user):
        """
        Raise authentication error if user is not from staff, or is inactive.
        """
        if not user.is_staff:
            raise ValidationError(
                self.error_messages["unauthorized"],
                code="unauthorized",
            )
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )
