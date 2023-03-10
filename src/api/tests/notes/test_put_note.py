import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from mixer.backend.django import mixer

from api.internal.models.notes import Note
from api.tests.utils import generate_random_index, put_request


@pytest.mark.django_db
def test_put_notes_without_user():
    response = put_request(reverse('notes-detail', args=(generate_random_index(),)))
    assert response.status_code == 401


@pytest.mark.django_db
def test_put_note_succsess(user, note):
    data = dict(title='new_title', description='new_description')
    response = put_request(reverse('notes-detail', args=(note.id,)), user=user, data=data)
    assert response.status_code == 200

    db_note = Note.objects.filter(id=note.id).first()
    assert db_note.description == data['description']
    assert db_note.title == data['title']


@pytest.mark.django_db
def test_put_unexisting_note(user):
    response = put_request(reverse('notes-detail', args=(generate_random_index(),)), user=user)
    assert response.status_code == 404


@pytest.mark.django_db
def test_put_not_user_record(user, note2):
    data = dict(title='new_title', description='new_description')
    response = put_request(reverse('notes-detail', args=(note2.id,)), user=user, data=data)
    assert response.status_code == 404

    db_note = Note.objects.filter(id=note2.id).first()
    assert db_note.description == 'description'
    assert db_note.title == 'title'
