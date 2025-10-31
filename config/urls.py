"""
URL configuration for config project.
"""

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, documento_root=settings.STATIC_ROOT)
        + debug_toolbar_urls()
    )
