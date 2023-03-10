import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from mixer.backend.django import mixer

from api.internal.models.notes import Note
from api.tests.utils import post_request


@pytest.mark.django_db
def test_create_note_succsess(user):
    data = dict(title='title', description='description')

    assert Note.objects.filter(user=user).count() == 0

    response = post_request(reverse('notes-list'), user=user, data=data)
    assert response.status_code == 201

    assert Note.objects.filter(user=user).count() == 1


@pytest.mark.django_db
def test_create_note_without_user():
    data = dict(title='title', description='description')
    response = post_request(reverse('notes-list'), data=data)

    assert response.status_code == 401


@pytest.mark.django_db
def test_create_note_without_data(user):
    response = post_request(reverse('notes-list'), user=user)

    assert response.status_code == 400
