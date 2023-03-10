import pytest
from django.urls import reverse
from django.contrib.auth.models import User

from api.tests.utils import post_request, create_jwt_token


@pytest.mark.django_db
def test_token_refresh(user):
    create_jwt_token(user)
    data = dict(refresh=user.refresh)
    response = post_request(reverse('token_refresh'), user=user, data=data)
    assert response.status_code == 200

    response_data = response.json()
    assert response_data['access']


@pytest.mark.django_db
def test_token_refresh_without_token():
    response = post_request(reverse('token_refresh'))
    assert response.status_code == 400
