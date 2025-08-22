from django.contrib import admin

from .models import Endereco


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "logradouro",
        "numero",
        "complemento",
        "bairro",
        "municipio",
        "estado",
        "cep",
    )
    search_fields = ("cliente__nome", "logradouro", "bairro", "municipio", "cep")
    list_filter = ("estado",)
    list_per_page = 20
