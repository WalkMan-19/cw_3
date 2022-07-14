from flask import Blueprint, jsonify
from posts.dao.posts_dao import PostsDAO

api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao = PostsDAO("./data/data.json")


@api_blueprint.route('/api/posts/')
def api_posts_page():
    posts = posts_dao.get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def api_post_page(post_id):
    post = posts_dao.get_post_by_pk(pk=post_id)
    return jsonify(post)
