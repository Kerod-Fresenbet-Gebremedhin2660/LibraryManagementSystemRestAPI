import pytest
import requests
import json


@pytest.fixture
def api():
    return "https://reqres.in"


@pytest.mark.skip
def test_success_login(api):
    url = api + "/api/v1/login"
    data = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == "INSERTTOKENHERE"


@pytest.mark.skip
def test_unsuccessful_login(api):
    url = api + "/api/v1/login"
    data = {'email': 'henok@gmail.com', 'password': 'pass'}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == "INSERT TOKEN HERE"


@pytest.mark.skip
def test_nopassword_login(api):
    url = api + "/api/v1/login"
    data = {'henok@gmail.com': ''}
    response = requests.post(url, data=data)
    error = json.loads(response.text)
    assert response.status_code == 200
    assert error['error'] == "Missing password"


@pytest.mark.skip
def test_single_user_get(api):
    url = api + "/api/users/21331312"
    response = requests.get(url)
    responsedata = json.loads(response.text)
    assert response.status_code == 200


@pytest.mark.skip
def test_create_user(api):
    url = api + "/api/v1/students"
    data = {"name": "henok", "sex": "F"}
    response = requests.post(url, data=data)
    responsedata = json.loads(response.text)
    assert response.status_code == 201
    assert responsedata["job"] == "leader"


@pytest.mark.skip
def test_update(api):
    url = api + "/api/student/2"
    data = {"name": "henok", "sex": "F"}
    response = requests.put(url, data=data)
    responsedata = json.loads(response.text)
    assert response.status_code == 200
    assert responsedata["job"] == "zion resident"


@pytest.mark.skip
def test_patch_update(api):
    url = api + "/api/users/2"
    data = {"name": "morpheus", "job": "zebegna"}
    response = requests.patch(url, data=data)
    responsedata = json.loads(response.text)
    assert response.status_code == 200
    assert responsedata["job"] == "zebegna"


@pytest.mark.skip
def test_delete(api):
    url = api + "/api/users/2"
    response = requests.delete(url)
    assert response.status_code == 204


@pytest.mark.skip
def test_registration(api):
    url = api + "/api/register/"
    data = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == "QpwL5tke4Pnpja7X4"
