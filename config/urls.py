"""
URL configuration for config project.
"""

from debug_toolbar.toolbar import debug_toolbar_urls  # noqa: I001
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("gelias.urls", namespace="gelias")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += (
        static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
        + debug_toolbar_urls()
    )
