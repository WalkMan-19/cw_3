from flask import Blueprint, render_template, request
from posts.dao.posts_dao import PostsDAO
from comments.dao.comments_dao import CommentsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")

posts_dao = PostsDAO("./data/data.json")
comments_dao = CommentsDAO("./data/comments.json")


@posts_blueprint.route('/')
def main_page():
    posts = posts_dao.get_posts_all()
    return render_template('index.html', posts=posts)


@posts_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    post = posts_dao.get_post_by_pk(post_id)
    comments = comments_dao.get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, comments=comments)


@posts_blueprint.route('/search/')
def search_page():
    s = request.args.get('s', '')
    posts = posts_dao.search_for_posts(s)
    return render_template('search.html', posts=posts, s=s)


@posts_blueprint.route('/users/<username>')
def user_page(username):
    try:
        posts = posts_dao.get_posts_by_user(username)
        return render_template('user-feed.html', posts=posts)
    except ValueError:
        return f"Пользователь {username} не найден"
