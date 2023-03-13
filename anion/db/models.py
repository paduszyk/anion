from django.db import models
from django.db.models import *  # noqa: F401, F403
from django.urls import reverse


class Model(models.Model):
    """
    Base class for all the models defined in the project.
    """

    class Meta:
        abstract = True

    @classmethod
    @property
    def opts(cls):
        """
        Return the model's meta options.

        The method enables referring to the options in templates.
        """
        return cls._meta

    @classmethod
    def _admin_action_url(cls, action, *args):
        """
        Return the URL for one of the admin site actions referring a model or
        its instance (the actions built-in are: "changelist," "add", "change",
        or "delete").
        """
        from anion.contrib.admin import site

        opts = cls.opts
        info = site.name, opts.app_label, opts.model_name
        return reverse("{}:{}_{}_{}".format(*info, action), args=args)

    @classmethod
    def admin_changelist_url(cls):
        """
        Return URL referring the model's admin changelist view.
        """
        return cls._admin_action_url("changelist")

    @classmethod
    def admin_add_url(cls):
        """
        Return URL referring the model's admin add form view.
        """
        return cls._admin_action_url("add")

    def admin_change_url(self):
        """
        Return URL referring the objects's admin change form view.
        """
        return self._admin_action_url("change", self.id)

    def admin_delete_url(self):
        """
        Return URL referring the objects's admin delete action view.
        """
        return self._admin_action_url("delete", self.id)
