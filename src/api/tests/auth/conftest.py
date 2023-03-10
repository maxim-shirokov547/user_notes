import pytest
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from mixer.backend.django import mixer

@pytest.fixture()
def user():
    return mixer.blend(User, username='username', password=make_password('password'))