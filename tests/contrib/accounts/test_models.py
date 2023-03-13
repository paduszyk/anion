from django.test import TestCase

from anion.contrib.accounts.models import Group, User


class GroupTestCase(TestCase):
    fixtures = [
        "accounts.json",
    ]

    def setUp(self):
        self.users_who_can_view = Group.objects.get(name="users-who-can-view")

    def test_str(self):
        self.assertEqual(str(self.users_who_can_view), "users-who-can-view")

    def test_natural_key(self):
        self.assertEqual(
            self.users_who_can_view.natural_key(), ("users-who-can-view",)
        )


class UserTestCase(TestCase):
    fixtures = [
        "accounts.json",
    ]

    @classmethod
    def setUpTestData(cls):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def setUp(self):
        self.active_user = User.objects.get(username="active-user")

    def test_str(self):
        self.assertEqual(str(self.active_user), "active-user")

    def test_natural_key(self):
        self.assertEqual(self.active_user.natural_key(), ("active-user",))

    def test_get_short_name(self):
        self.assertEqual(self.active_user.get_short_name(), "active-user")

    def test_get_full_name(self):
        self.assertEqual(self.active_user.get_full_name(), "active-user")
