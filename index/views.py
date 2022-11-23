from flask import Blueprint, render_template
from utils import load_posts

index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates')


@index_blueprint.get('/')
def index_page():
    posts = load_posts()
    return render_template('index.html', posts=posts)
