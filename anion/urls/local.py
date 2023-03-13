from django.urls import include, path

from .base import urlpatterns

try:
    import debug_toolbar  # noqa: F401
except ImportError:
    pass
else:
    urlpatterns += [
        path("debug-toolbar/", include("debug_toolbar.urls")),
    ]
