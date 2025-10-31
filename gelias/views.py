from django.http import HttpRequest, HttpResponse  # noqa: I001
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Página Inicial"""

    return render(request, "gelias/index.html")
