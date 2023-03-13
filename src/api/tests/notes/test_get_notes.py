import pytest
from django.urls import reverse

from api.tests.utils import generate_random_index, get_request


@pytest.mark.django_db
def test_get_notes_without_user():
    response = get_request(reverse('notes-list'))
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_empty_notes(user):
    response = get_request(reverse('notes-list'), user=user)
    assert response.status_code == 200

    response_data = response.json().get('results', [])
    assert response_data == []


@pytest.mark.django_db
def test_get_notes(user, note, note2):
    response = get_request(reverse('notes-list'), user=user)
    assert response.status_code == 200

    response_data = response.json().get('results', [])
    assert len(response_data) == 1

    check_note(response_data[0])


@pytest.mark.django_db
def test_get_note_by_id_succsess(user, note):
    response = get_request(reverse('notes-detail', args=(note.id,)), user=user)
    assert response.status_code == 200

    check_note(response.json())


@pytest.mark.django_db
def test_get_unexisting_note(user):
    response = get_request(reverse('notes-detail', args=(generate_random_index(),)), user=user)
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_note_without_user(note):
    response = get_request(reverse('notes-detail', args=(note.id,)))
    assert response.status_code == 401


def check_note(data):
    assert data['title'] == 'title'
    assert data['description'] == 'description'
