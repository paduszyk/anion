from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission

from .models import User


class ModelBackend(ModelBackend):
    """
    Authentication backend for `accounts.User` users.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Return the authenticated user or `None` if authentication fails.

        If user tries to authenticate using e-mail, get the user and
        override the passed credentials by the actual username. Then
        attempt to proceed using the base class method.
        """
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            pass
        else:
            username = user.username
        return super().authenticate(request, username, password, **kwargs)

    def user_can_authenticate(self, user):
        """
        Allow all the user to authenticate, regardless they are active or not
        (as defined in the base backend).
        """
        return True

    def _get_group_permissions(self, user_obj):
        """
        Modify the permissions queryset by referring to the backend's app group
        model instead of the `auth.Group` as in the base backend.
        """
        return Permission.objects.filter(groups__users=user_obj)
