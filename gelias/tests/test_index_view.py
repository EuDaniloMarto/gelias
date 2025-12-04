from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_cd_status_ok(client):
    request = client.get(reverse("gelias:index"))
    assert request.status_code == HTTPStatus.OK
