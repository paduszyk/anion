from django.contrib.auth.models import AbstractUser, Permission, UserManager
from django.core.validators import EmailValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

from anion.db import models
from anion.db.models import Q


class GroupManager(models.Manager):
    """
    Default manager of the `accounts.Group` model.
    """

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Group(models.Model):
    """
    Model representing groups of the site users.
    """

    name = models.CharField(
        _("name"),
        max_length=255,
        unique=True,
        error_messages={
            "unique": _("Group with that name already exists."),
        },
    )
    permissions = models.ManyToManyField(
        Permission,
        related_name="groups",
        blank=True,
        verbose_name=Permission._meta.verbose_name_plural,
    )

    objects = GroupManager()

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class UserManager(UserManager):
    """
    Default manager of the `accounts.User` model.
    """

    def get_by_natural_key(self, username_or_email):
        """
        Compared to the base manager, the `accounts.User` objects can be
        deserialized using either username or e-mail address.
        """
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username_or_email})
            | Q(**{self.model.EMAIL_FIELD: username_or_email})
        )


class User(models.Model, AbstractUser):
    """
    Model representing the site users.
    """

    # Identifiers and authentication fields
    username = models.CharField(
        _("username"),
        max_length=255,
        unique=True,
        validators=[
            RegexValidator(
                r"[a-zA-Z0-9_.-]{3,}",
                message=_(
                    "Valid username must be of length of least 3 chars and "
                    "contain only ASCII characters/dots/hyphens/underscores."
                ),
            )
        ],
        error_messages={
            "unique": _("User with that username already exists."),
        },
    )
    email = models.CharField(
        _("e-mail address"),
        max_length=255,
        unique=True,
        validators=[
            EmailValidator(message=_("Invalid e-mail address format.")),
        ],
        error_messages={
            "unique": _("Group with that e-mail address already exists."),
        },
    )

    # Personal data - discarded (handled by the `staff.Person` model)
    last_name = None
    first_name = None

    # Roles and permissions fields
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("administrator"), default=False)
    is_superuser = models.BooleanField(_("superuser"), default=False)
    groups = models.ManyToManyField(
        Group,
        related_name="users",
        verbose_name=Group._meta.verbose_name_plural,
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="users",
        verbose_name=Permission._meta.verbose_name_plural,
        blank=True,
    )

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.get_username()

    def natural_key(self):
        """
        Serialize the user object as its `username` field value.
        """
        return (self.username,)

    def get_short_name(self):
        """
        Base class implementation discarded as it's uses personal data fields,
        which are excluded in this model.
        """
        return self.get_username()

    def get_full_name(self):
        """
        Base class implementation discarded as it's uses personal data fields,
        which are excluded in this model.
        """
        return self.get_username()
