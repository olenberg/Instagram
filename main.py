from flask import Flask, render_template, jsonify
from index.views import index_blueprint
from post.views import post_blueprint
from search.views import search_blueprint
from user_feed.views import user_feed_blueprint
from bookmarks.views import bookmarks_blueprint
from tag.views import tag_blueprint
from utils import load_posts, get_post_by_pk
import logging

logging.basicConfig(filename='logs/api.log', level=logging.INFO)
logger = logging.getLogger("logger")
file_handler = logging.FileHandler('logs/api.log')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

app = Flask(__name__)

app.register_blueprint(index_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(bookmarks_blueprint)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.get('/api/posts')
def api_get_posts():
    posts = load_posts()
    logger.info('Запрос /api/posts')
    return jsonify(posts)


@app.get('/api/posts/<int:post_id>')
def api_get_post_by_id(post_id):
    post = get_post_by_pk(post_id)
    logger.info(f'Запрос /api/posts/{post_id}')
    return jsonify(post)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

