from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from anion.contrib.accounts.models import User


class ModelBackendTestCase(TestCase):
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
        self.inactive_user = User.objects.get(username="inactive-user")
        self.staff_user = User.objects.get(username="staff-user")

    def tearDown(self):
        self.client.logout()

    def test_user_can_authenticate_using_username(self):
        authenticated = self.client.login(
            username=self.active_user.username, password="password"
        )
        self.assertTrue(authenticated)

    def test_user_can_authenticate_using_email(self):
        authenticated = self.client.login(
            username=self.active_user.email, password="password"
        )
        self.assertTrue(authenticated)

    def test_user_can_authenticate_even_if_inactive(self):
        authenticated = self.client.login(
            username=self.inactive_user.username, password="password"
        )
        self.assertTrue(authenticated)

    def test_group_permissions(self):
        # Login as the staff user belonging to a group with view permissions
        self.client.login(
            username=self.staff_user.username, password="password"
        )

        # Try to access the list of books (permissions granted)
        response = self.client.get(reverse("admin:tests_book_changelist"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Try to access the add form for a new book (permissions not granted)
        response = self.client.get(reverse("admin:tests_book_add"))
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)
