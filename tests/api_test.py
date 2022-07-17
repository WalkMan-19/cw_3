import pytest
from run import app

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_api_posts():
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200, "Неверный статус-код"
    assert type(response.json) == list, "Возвращается не список"
    assert len(response.json) > 0, "Пустой список"
    assert set(response.json[0].keys()) == keys_should_be, "Возвращается не верный список ключей для постов"


def test_api_single_post():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200, "Неверный статус-код"
    assert type(response.json) == dict, "Возвращается не словарь для одного пользователя"
    assert set(response.json.keys()) == keys_should_be, "Возвращается не верный список ключей"
