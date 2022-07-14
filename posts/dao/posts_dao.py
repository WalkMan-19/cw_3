import json
from json import JSONDecodeError


class PostsDAO:

    def __init__(self, path):
        """
        При создании экземпляра DAO указываем путь к файлу с данными
        """
        self.path = path

    def load_posts_json(self):
        """
        Загружаем данные из JSON-файла
        :return: list[dict]
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                response = json.load(f)
            return response
        except JSONDecodeError:
            return "Не удалось преобразовать файл"
        except FileNotFoundError:
            return "Файл не найден"

    def get_posts_all(self) -> list[dict]:
        """ Все посты """
        posts = self.load_posts_json()
        return posts

    def get_posts_by_user(self, user_name: str):
        """ Возвращает нужный пост по ключевому пользователю """
        posts = self.get_posts_all()
        result = []
        for post in posts:
            if post['poster_name'] == user_name:
                result.append(post)
        return result

    def search_for_posts(self, query):
        """ Возвращает нужный пост по ключевому слову """
        posts = self.get_posts_all()
        result = []
        for post in posts:
            if query.lower() in post['content'].lower():
                result.append(post)
        return result

    def get_post_by_pk(self, pk: int):
        """ Возвращает нужный пост по его pk """
        posts = self.get_posts_all()
        for post in posts:
            if post['pk'] == pk:
                return post
