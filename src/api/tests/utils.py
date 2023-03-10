import time
from random import randint

from django.conf import settings
from django.http.response import HttpResponse
from django.test import Client
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

client = Client()


def generate_random_index():
    return randint(1735, int(time.time()))


def convert_headers_to_META(headers):
    return {f'HTTP_{header}': headers[header] for header in headers}


def create_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    setattr(user, 'refresh', str(refresh))
    return str(refresh.access_token)


def __request(url, type, data=None, query=None, multipart=False, user=None, headers=None):
    headers = {'AUTHORIZATION': f'Bearer {create_jwt_token(user)}'} if user and not headers else {}
    headers = convert_headers_to_META(headers)
    if type == 'get':
        return client.get(
            url,
            query,
            **headers,
            content_type='application/json',
        )
    if type in ['put', 'post']:
        if not multipart:
            headers['content_type'] = 'application/json'
        return getattr(client, type)(
            url,
            **headers,
            data=data,
        )
    if type == 'delete':
        return client.delete(
            url,
            **headers,
        )
    raise Exception(f'Wrong request type "{type}"')


def get_request(url, query={}, headers=None, user=None):
    return __request(url, 'get', query=query, user=user, headers=headers)


def post_request(url, data={}, multipart=False, headers=None, user=None):
    return __request(url, 'post', data=data, multipart=multipart, user=user, headers=headers)


def put_request(url, data={}, multipart=False, headers=None, user=None) -> HttpResponse:
    return __request(url, 'put', data=data, multipart=multipart, user=user, headers=headers)


def delete_request(url, headers=None, user=None) -> HttpResponse:
    return __request(url, 'delete', user=user, headers=headers)
