from django.utils.translation import gettext_lazy as _

from anion.db import models


class GroupManager(models.Manager):
    """
    Default manager of the `accounts.Group` model.
    """


class Group(models.Model):
    """
    Model representing groups of the site users.
    """

    objects = GroupManager()

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")


class UserManager(models.Manager):
    """
    Default manager of the `accounts.User` model.
    """


class User(models.Model):
    """
    Model representing the site users.
    """

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
