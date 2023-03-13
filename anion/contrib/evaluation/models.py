from django.utils.translation import gettext_lazy as _

from anion.db import models


class DegreeManager(models.Manager):
    """
    Default manager of the `evaluation.Degree` model.
    """


class Degree(models.Model):
    """
    Model representing academic degrees.
    """

    objects = DegreeManager()

    class Meta:
        verbose_name = _("degree")
        verbose_name_plural = _("degrees")


class DomainManager(models.Manager):
    """
    Default manager of the `evaluation.Domain` model.
    """


class Domain(models.Model):
    """
    Model representing domains of science.
    """

    objects = DomainManager()

    class Meta:
        verbose_name = _("domain")
        verbose_name_plural = _("domains")


class DisciplineManager(models.Manager):
    """
    Default manager of the `evaluation.Discipline` model.
    """


class Discipline(models.Model):
    """
    Model representing disciplines of science.
    """

    objects = DisciplineManager()

    class Meta:
        verbose_name = _("discipline")
        verbose_name_plural = _("disciplines")
