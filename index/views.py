from flask import Blueprint, render_template
from utils import load_posts, load_bookmarks

index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates')


@index_blueprint.get('/')
def index_page():
    posts = load_posts()
    bookmarks = load_bookmarks()
    return render_template('index.html', posts=posts, bookmarks=bookmarks)
