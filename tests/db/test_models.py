from django.test import TestCase
from django.urls import reverse

from anion.contrib import admin

from tests.models import Book


class ModelTestCase(TestCase):
    fixtures = [
        "tests.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.get(title="Moby Dick")
        cls.info = (
            admin.site.name,
            Book._meta.app_label,
            Book._meta.model_name,
        )

    def test_opts_by_class(self):
        self.assertEqual(Book.opts, Book._meta)

    def test_opts_by_obj(self):
        self.assertEqual(self.book.opts, self.book._meta)

    def test_admin_changelist_url(self):
        url = self.book.admin_changelist_url()
        self.assertEqual(
            url,
            reverse("{}:{}_{}_changelist".format(*self.info)),
        )

    def test_admin_add_url(self):
        url = self.book.admin_add_url()
        self.assertEqual(
            url,
            reverse("{}:{}_{}_add".format(*self.info)),
        )

    def test_admin_change_url(self):
        url = self.book.admin_change_url()
        self.assertEqual(
            url,
            reverse(
                "{}:{}_{}_change".format(*self.info),
                args=(self.book.id,),
            ),
        )

    def test_admin_delete_url(self):
        url = self.book.admin_delete_url()
        self.assertEqual(
            url,
            reverse(
                "{}:{}_{}_delete".format(*self.info),
                args=(self.book.id,),
            ),
        )
