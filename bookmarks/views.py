from flask import Blueprint, render_template, redirect, request
from utils import load_bookmarks, add_bookmark, delete_bookmark

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


@bookmarks_blueprint.get('/bookmarks')
def bookmarks_page():
    bookmarks = load_bookmarks()
    return render_template('bookmarks.html', bookmarks=bookmarks)


@bookmarks_blueprint.post('/bookmarks/add')
def add_post_to_bookmarks():
    post_id = int(request.form.get('post_id'))
    add_bookmark(post_id)
    return redirect('/', 302)


@bookmarks_blueprint.post('/bookmarks/delete')
def delete_post_from_bookmarks():
    bookmark_id = int(request.form.get('bookmark_id'))
    delete_bookmark(bookmark_id)
    return redirect('/', 302)
