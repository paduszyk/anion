from django.utils.translation import gettext_lazy as _

from anion.db import models

__all__ = [
    "Journal",
]


class PublisherManager(models.Manager):
    """
    Default manager of the `output.Publisher` model.
    """


class Publisher(models.Model):
    """
    Model representing publishers.
    """

    objects = PublisherManager()

    class Meta:
        verbose_name = _("publisher")
        verbose_name_plural = _("publishers")


class JournalManager(models.Manager):
    """
    Default manager of the `output.Journal` model.
    """


class Journal(models.Model):
    """
    Model representing scientific journals.
    """

    objects = JournalManager()

    class Meta:
        verbose_name = _("journal")
        verbose_name_plural = _("journals")
