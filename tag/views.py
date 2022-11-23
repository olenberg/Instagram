from flask import Blueprint, render_template
from utils import get_posts_by_tag

tag_blueprint = Blueprint('tag_blueprint', __name__, template_folder='templates')


@tag_blueprint.get('/tag/<tag>')
def tag_page(tag):
    posts = get_posts_by_tag(tag)
    return render_template('tag.html', posts=posts, tag=tag)
