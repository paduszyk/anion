from django.utils.translation import gettext_lazy as _

from anion.db import models

__all__ = [
    "Article",
    "Award",
    "Book",
    "Patent",
    "Project",
]


class AbstractWorkManager(models.Manager):
    """
    Base class for managers of the models based on the `AbstractWork` class.
    """


class AbstractWork(models.Model):
    """
    Abstract model representing common features of all the types of the
    output's works (like articles, books, patents, projects, awards).
    """

    objects = AbstractWorkManager()

    class Meta:
        abstract = True


class ArticleManager(models.Manager):
    """
    Default manager of the `output.Article` model.
    """


class Article(AbstractWork):
    """
    Model representing articles published in scientific journals.
    """

    objects = ArticleManager()

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")


class BookManager(models.Manager):
    """
    Default manager of the `output.Book` model.
    """


class Book(AbstractWork):
    """
    Model representing books or book chapters.
    """

    objects = BookManager()

    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("books")


class PatentManager(models.Manager):
    """
    Default manager of the `output.Patent` model.
    """


class Patent(AbstractWork):
    """
    Model representing patents.
    """

    objects = PatentManager()

    class Meta:
        verbose_name = _("patent")
        verbose_name_plural = _("patents")


class ProjectManager(models.Manager):
    """
    Default manager of the `output.Project` model.
    """


class Project(AbstractWork):
    """
    Model representing projects (grants).
    """

    objects = ProjectManager()

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")


class AwardManager(models.Manager):
    """
    Default manager of the `output.Award` model.
    """


class Award(AbstractWork):
    """
    Model representing awards.
    """

    objects = AwardManager()

    class Meta:
        verbose_name = _("award")
        verbose_name_plural = _("awards")
