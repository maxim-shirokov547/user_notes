import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from mixer.backend.django import mixer

from api.tests.utils import create_jwt_token, post_request


@pytest.mark.django_db
def test_log_out_success(user):
    token = create_jwt_token(user)
    data = dict(refresh=user.refresh)
    response = post_request(reverse('log_out'), user=user, data=data)
    assert response.status_code == 200

    response = post_request(reverse('log_out'), user=user, headers=dict(AUTHORIZATION=token))
    assert response.status_code == 401


@pytest.mark.django_db
def test_log_out_without_refresh_token(user):
    response = post_request(reverse('log_out'), user=user)
    assert response.status_code == 400


@pytest.mark.django_db
def test_log_out_without_user() -> None:
    response = post_request(reverse('log_out'))
    assert response.status_code == 401
