from django.urls import path

from . import views

app_name = "crm"

urlpatterns = [
    path("", views.ir_para_lista_clientes, name="ir_para_lista_clientes"),
]
