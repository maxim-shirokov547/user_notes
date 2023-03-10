import pytest
from django.urls import reverse
from django.contrib.auth.models import User

from mixer.backend.django import mixer
from api.tests.utils import delete_request, generate_random_index

from api.internal.models.notes import Note


@pytest.mark.django_db
def test_delete_notes_without_user():
    response = delete_request(reverse(f'notes-detail', args=(generate_random_index(),)))
    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_note_succsess(user, note):
    response = delete_request(reverse(f'notes-detail', args=(note.id,)), user=user)
    assert response.status_code == 204

    assert not Note.objects.filter(id=note.id).first()


@pytest.mark.django_db
def test_delete_unexisting_note(user, note):
    response = delete_request(reverse(f'notes-detail', args=(generate_random_index(),)), user=user)
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_not_user_record(user, note2):
    response = delete_request(reverse(f'notes-detail', args=(note2.id,)), user=user)
    assert response.status_code == 404

    assert Note.objects.filter(id=note2.id).first()
