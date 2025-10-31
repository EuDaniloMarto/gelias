from django.urls import path

from . import views

app_name = "gelias"

urlpatterns = [
    path("", views.index, name="index"),
]
