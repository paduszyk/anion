from django.utils.translation import gettext_lazy as _

from anion.db import models

__all__ = [
    "Contract",
    "Group",
    "Position",
    "Status",
]


class GroupManager(models.Manager):
    """
    Default manager of the `staff.Group` model.
    """


class Group(models.Model):
    """
    Model representing groups of persons.
    """

    objects = GroupManager()

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")


class PositionManager(models.Manager):
    """
    Default manager of the `staff.Position` model.
    """


class Position(models.Model):
    """
    Model representing positions persons can be employed at.
    """

    objects = PositionManager()

    class Meta:
        verbose_name = _("position")
        verbose_name_plural = _("positions")


class StatusManager(models.Manager):
    """
    Default manager of the `staff.Status` model.
    """


class Status(models.Model):
    """
    Model representing contract statuses.
    """

    objects = StatusManager()

    class Meta:
        verbose_name = _("status")
        verbose_name_plural = _("statuses")


class ContractManager(models.Manager):
    """
    Default manager of the `staff.Contract` model.
    """


class Contract(models.Model):
    """
    Model representing contracts.

    Contract consists of information about the mutual relationships
    between persons, positions and units.
    """

    objects = ContractManager()

    class Meta:
        verbose_name = _("contract")
        verbose_name_plural = _("contracts")
