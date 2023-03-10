import pytest
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from mixer.backend.django import mixer

from api.internal.models.notes import Note


@pytest.fixture()
def user():
    return mixer.blend(User, username='username', password=make_password('password'))


@pytest.fixture()
def user2():
    return mixer.blend(User, username='username2', password=make_password('password2'))


@pytest.fixture()
def note(user):
    return mixer.blend(Note, title='title', description='description', user=user)


@pytest.fixture()
def note2(user2):
    return mixer.blend(Note, title='title', description='description', user=user2)
