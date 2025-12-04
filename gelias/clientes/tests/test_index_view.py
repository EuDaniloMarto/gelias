from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.fixture
def url():
    return reverse("clientes:index")


@pytest.mark.django_db
def test_cd_status_302(client, url):
    response = client.get(url)
    assert response.status_code == HTTPStatus.FOUND


@pytest.mark.django_db
def test_cd_status_200(client_logged, url):
    response = client_logged.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_contexto_pagina(client_logged, url):
    response = client_logged.get(url)
    assert "pagina" in response.context
    assert response.context.get("pagina") == "clientes"
