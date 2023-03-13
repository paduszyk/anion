from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from anion.contrib import admin

from .. import views

# Base URLs

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]


# App URLs

urlpatterns += []


# Admin site URLs

urlpatterns += [
    path("admin/", admin.site.urls),
]


# Static and media files URLs

urlpatterns = (
    urlpatterns
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
