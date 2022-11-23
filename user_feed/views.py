from flask import Blueprint, render_template
from utils import get_posts_by_username

user_feed_blueprint = Blueprint('user_feed_blueprint', __name__, template_folder='templates')


@user_feed_blueprint.get('/users/<username>')
def user_feed_page(username):
    posts = get_posts_by_username(username)
    return render_template('user-feed.html', posts=posts, username=username)
