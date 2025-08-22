from django.urls import include, path

from . import views

app_name = "clientes"

urlpatterns = [
    path(
        "criar/",
        views.criar_clientes,
        name="criar_cliente",
    ),
    path(
        "<slug:slug>/",
        include(
            [
                path(
                    "",
                    views.ver_cliente,
                    name="ver_cliente",
                ),
                path(
                    "atualizar/",
                    views.atualizar_cliente,
                    name="atualizar_cliente",
                ),
                path(
                    "enderecos/",
                    include("CRM.enderecos.urls", namespace="enderecos"),
                ),
            ],
        ),
    ),
    path(
        "servico/<str:tipo_servico>/",
        views.listar_clientes,
        name="listar_clientes_por_tipo_servico",
    ),
    path(
        "",
        views.listar_clientes,
        name="listar_clientes",
    ),
]
