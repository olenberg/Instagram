from flask import Blueprint, request, render_template
from utils import search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.get('/search')
def search_page():
    query = request.args.get('s')
    if query == '':
        return 'Введён пустой поисковый запрос'
    posts = search_for_posts(query)
    return render_template('search.html', posts=posts)
