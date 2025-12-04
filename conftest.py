import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def client_logged(client):
    user = get_user_model().objects.create_user(username="fulano")
    client.force_login(user)
    yield client
    user.delete()
