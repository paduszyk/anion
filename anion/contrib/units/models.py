from django.utils.translation import gettext_lazy as _

from anion.db import models


class AbstractUnitManager(models.Manager):
    """
    Base class for managers of the models based on the `AbstractUnit` class.
    """


class AbstractUnit(models.Model):
    """
    Abstract model representing common features of all the types of units.
    """

    objects = AbstractUnitManager()

    class Meta:
        abstract = True


class InstitutionManager(models.Manager):
    """
    Default manager of the `units.Institution` model.
    """


class Institution(AbstractUnit):
    """
    Model representing institutions.

    Institutions are on the top of the units' hierarchy.
    """

    objects = InstitutionManager()

    class Meta:
        verbose_name = _("institution")
        verbose_name_plural = _("institutions")


class InstituteManager(models.Manager):
    """
    Default manager of the `units.Institute` model.
    """


class Institute(AbstractUnit):
    """
    Model representing institutes.

    Institutes are the units that institutions are consisted of.
    """

    objects = InstituteManager()

    class Meta:
        verbose_name = _("institute")
        verbose_name_plural = _("institutes")


class DepartmentManager(models.Manager):
    """
    Default manager of the `units.Department` model.
    """


class Department(AbstractUnit):
    """
    Model representing departments.

    Departments are the units that institutes are consisted of.
    """

    objects = DepartmentManager()

    class Meta:
        verbose_name = _("department")
        verbose_name_plural = _("departments")
