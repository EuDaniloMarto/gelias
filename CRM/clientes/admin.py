from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "tipo_cliente",
    )
    prepopulated_fields = {"slug": ("nome",)}
    search_fields = ("nome",)
    list_filter = ("tipo_cliente", "ativo", "alarme", "camera")
    ordering = ("nome", "ativo")
    date_hierarchy = "criado_em"
