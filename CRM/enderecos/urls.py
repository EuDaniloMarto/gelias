from django.urls import path

from . import views

app_name = "enderecos"

urlpatterns = [
    path("criar/", views.criar_endereco, name="criar_endereco"),
]
