from posts.dao.posts_dao import PostsDAO

posts_dao = PostsDAO('../data/data.json')


class TestMain:
    def test_root_status(self, test_client):
        """Проверяем статус-код"""
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус-код неверный"

    def test_root_content(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert posts_dao.get_posts_all() in response.data.decode('utf-8'), "Контент неверный"

