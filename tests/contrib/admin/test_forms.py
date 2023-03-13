from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from anion.contrib.admin.forms import AdminAuthenticationForm

User = get_user_model()


class AdminAuthenticationFormTestCase(TestCase):
    def setUp(self):
        self.form = AdminAuthenticationForm()

    def create_user(self, **extra_fields):
        return User.objects.create_user(
            username="user",
            email="user@anion.tests",
            password="password",
            **extra_fields,
        )

    def test_username_label_has_username_field_label(self):
        username_label = self.form.fields["username"].label.lower()
        self.assertIn(
            str(User._meta.get_field(User.USERNAME_FIELD).verbose_name),
            username_label,
        )

    def test_username_label_has_email_field_label(self):
        username_label = self.form.fields["username"].label.lower()
        self.assertIn(
            str(User._meta.get_field(User.EMAIL_FIELD).verbose_name),
            username_label,
        )

    def test_confirm_login_allowed_if_not_staff_user(self):
        user = self.create_user(is_active=True, is_staff=False)
        with self.assertRaisesMessage(
            ValidationError,
            str(self.form.error_messages["unauthorized"]),
        ):
            self.form.confirm_login_allowed(user)

    def test_confirm_login_allowed_if_not_active_staff_user(self):
        user = self.create_user(is_active=False, is_staff=True)
        with self.assertRaisesMessage(
            ValidationError,
            str(self.form.error_messages["inactive"]),
        ):
            self.form.confirm_login_allowed(user)

    def test_confirm_login_allowed_if_active_staff_user(self):
        user = self.create_user(is_active=True, is_staff=True)
        try:
            self.form.confirm_login_allowed(user)
        except ValidationError:
            self.fail()
