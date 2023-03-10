import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from mixer.backend.django import mixer

from api.tests.utils import post_request


@pytest.mark.django_db
def test_sign_up_success() -> None:
    data = dict(username='username', password='password')
    response = post_request(reverse('sign_up'), data=data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_sign_up_username_conflict() -> None:
    mixer.blend(User, username='username')
    data = dict(username='username', password='password')
    response = post_request(reverse('sign_up'), data=data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_sign_up_without_username() -> None:
    data = dict(password='password')
    response = post_request(reverse('sign_up'), data=data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_sign_up_without_password():
    data = dict(username='username')
    response = post_request(reverse('sign_up'), data=data)
    assert response.status_code == 400
