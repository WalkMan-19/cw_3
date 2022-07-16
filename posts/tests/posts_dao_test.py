import pytest
from posts.dao.posts_dao import PostsDAO


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO("data_moc.json")
    return posts_dao_instance


keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

key_for_search_for_posts = "Очень красивый закат. Стоило выбраться из дома, чтобы посмотреть на него! а где ты был?"


class TestPostsDao:

    def test_get_all(self, posts_dao):
        """Проверяем, верный ли список постов возвращается"""
        posts = posts_dao.get_posts_all()
        assert type(posts) == list[dict], "Возвращается не список, словарей"
        assert len(posts) > 0, "Возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "Неверный список ключей"

    def test_get_posts_by_user(self, posts_dao):
        """Проверяем, верный ли пост возвращается при запросе по нику пользователя"""
        posts = posts_dao.get_posts_by_user("leo")
        for post in posts:
            assert post["poster_name"] == "leo", "Возвращается неправильный пользователь"
            assert set(post.keys()) == keys_should_be, "Неверный список ключей"

    def test_search_for_posts(self, posts_dao):
        """Проверяем, верный ли пост возвращается при запросе по контенту"""
        posts = posts_dao.search_for_posts("где")
        for post in posts:
            assert (post["content"] == key_for_search_for_posts), "Возвращается неправильный контент"

    def test_get_post_by_pk(self, posts_dao):
        """Проверяем, верный ли пост возвращается при запросе его pk"""
        post = posts_dao.get_post_by_pk(1)
        assert (post["pk"] == 1), "Возвращается неправильный pk"
        assert set(post.keys()) == keys_should_be, "Возвращается неправильный список ключей"
