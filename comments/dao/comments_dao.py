import json
from json import JSONDecodeError


class CommentsDAO:

    def __init__(self, path):
        self.path = path

    def load_comments_json(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                response = json.load(f)
            return response
        except JSONDecodeError:
            return "Файл не удалось преобразовать"
        except FileNotFoundError:
            return "Файл не найден"

    def get_comments_by_post_id(self, post_id: int):
        comments = self.load_comments_json()
        result = []
        for comment in comments:
            if comment['post_id'] == post_id:
                result.append(comment)
        return result
