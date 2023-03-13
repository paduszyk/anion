from django.utils.translation import gettext_lazy as _

from anion.db import models

__all__ = [
    "Author",
    "Contribution",
]


class AuthorManager(models.Manager):
    """
    Default manager of the `output.Author` model.
    """


class Author(models.Model):
    """
    Model representing authors of the output's works.

    Affiliated authors are related to works via their contracts.
    """

    objects = AuthorManager()

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")


class ContributionManager(models.Manager):
    """
    Default manager of the `output.Contribution` model.
    """


class Contribution(models.Model):
    """
    Model representing authors' contributions to the output's works.

    A need for such a model is because some extra data has to be tracked
    when relating an author to a work. Author itself is not enough.
    """

    objects = ContributionManager()

    class Meta:
        verbose_name = _("contribution")
        verbose_name_plural = _("contributions")
