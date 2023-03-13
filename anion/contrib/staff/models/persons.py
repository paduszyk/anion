from django.utils.translation import gettext_lazy as _

from anion.db import models

__all__ = [
    "Person",
]


class PersonManager(models.Manager):
    """
    Default manager of the `staff.Person` model.
    """


class Person(models.Model):
    """
    Model representing persons.

    Persons are uniquely related to users and store data like: personal
    data, evaluation data, etc.
    """

    objects = PersonManager()

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")
