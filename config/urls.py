"""URL configuration for CRM Elias project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("clientes/", include("CRM.clientes.urls", namespace="clientes")),
    path("admin/", admin.site.urls),
    path("", include("CRM.urls", namespace="crm")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        *urlpatterns,
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
        path("__debug__/", include(debug_toolbar.urls)),
    ]
