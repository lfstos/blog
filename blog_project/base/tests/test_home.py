from http import HTTPStatus
from django.shortcuts import resolve_url


def test_home_status_code(client):
    resp = client.get(resolve_url('base:home'))

    assert resp.status_code == HTTPStatus.OK
