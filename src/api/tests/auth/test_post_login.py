import pytest
from django.urls import reverse
from django.contrib.auth.models import User

from mixer.backend.django import mixer
from api.tests.utils import post_request


@pytest.mark.django_db
def test_login_success(user):
    data = dict(username='username', password='password')
    response = post_request(reverse('login'), data=data)
    assert response.status_code == 200

    response_data = response.json()
    assert response_data['refresh']
    assert response_data['access']


@pytest.mark.django_db
def test_login_invalid_credentials(user):
    data = dict(username='username', password='wrong')
    response = post_request(reverse('login'), data=data)
    assert response.status_code == 401
