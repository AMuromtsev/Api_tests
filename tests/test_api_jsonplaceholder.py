import requests
import pytest
import cerberus


@pytest.mark.parametrize('code', [200])  # валидация json
def test_get_jsonplaceholder_json_validation(base_url_jsonplaceholder, request_method, code):
    target = base_url_jsonplaceholder + 'posts/1'
    response = request_method(url=target)
    schema = {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "number"}
    }
    v = cerberus.Validator()
    assert response.status_code == code
    assert v.validate(response.json(), schema)


@pytest.mark.parametrize('code', [200])  # проверяем получение всех posts
def test_get_jsonplaceholder_all_posts(base_url_jsonplaceholder, request_method, code):
    target = base_url_jsonplaceholder + 'posts'
    response = request_method(url=target)
    assert response.status_code == code


  # проверяем создание, метод POST и валидируем json
def test_get_jsonplaceholder_create_posts(base_url_jsonplaceholder):
    target = base_url_jsonplaceholder + 'posts/'
    response = requests.post(target, headers=
    {
        'Content-type': 'application/json; charset:UTF-8'
    }, data={
        'title': 'foo',
        'body': 'bar_test',
        'userId': 1, })
    response.raise_for_status()
    schema = {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "number"}
    }
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)

@pytest.mark.parametrize('code', [200])  # проверяем обновление, метод PUT
def test_get_jsonplaceholder_update_posts(base_url_jsonplaceholder, request_method, code):
    target = base_url_jsonplaceholder + 'posts/'
    response = requests.put(target, headers=
    {
        'Content-type': 'application/json; charset:UTF-8'
    }, data={
    'id': 1,
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
  })
    schema = {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "number"}
    }
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)


@pytest.mark.parametrize('code', [200])  # проверяем метод DELETE
def test_delete_jsonplaceholder_post(base_url_jsonplaceholder, code):
    target = base_url_jsonplaceholder + 'posts/1'
    response = requests.delete(target)
    assert response.status_code == code
