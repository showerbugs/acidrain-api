import json

import pytest

from django.urls import reverse


class TestUserViewPost():
    @pytest.mark.django_db(transaction=True)
    @pytest.mark.parametrize('params', [{
        'name': 'qodot',
        'password': '1234',
    }])
    def test_success(self, client, params):
        url = reverse('users')
        json_params = json.dumps(params)
        resp = client.post(url, json_params, content_type='application/json')

        assert resp.status_code == 201
        assert resp.json().get('user')

    @pytest.mark.django_db(transaction=True)
    def test_no_request_body(self, client):
        url = reverse('users')
        resp = client.post(url, content_type='application/json')

        assert resp.status_code == 400
        assert resp.json().get('message') == 'no request body'

    # @pytest.mark.django_db(transaction=True)
    # def test_wrong_json(self, client):
    #     url = reverse('users')
    #     resp = client.post(url, content_type='application/json')

    #     assert resp.status_code == 400
    #     assert resp.json()['message'] == 'wrong json format'

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.parametrize('params', [{
        'name': 'qodot',
        'password': '1234',
    }])
    def test_duplicated_name(self, client, params, users):
        url = reverse('users')
        json_params = json.dumps(params)
        resp = client.post(url, json_params, content_type='application/json')

        assert resp.status_code == 409
        assert resp.json().get('message') == 'already existed name'
