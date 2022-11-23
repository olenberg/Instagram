from utils import load_posts, get_posts_by_username, get_comments_by_post_id, search_for_posts, get_post_by_pk


def test_load_posts():
    posts = load_posts()
    assert type(posts) == list
    assert type(posts[0]) == dict
    assert 'poster_name' in posts[0].keys()
    assert 'poster_avatar' in posts[0].keys()
    assert 'pic' in posts[0].keys()
    assert 'content' in posts[0].keys()
    assert 'views_count' in posts[0].keys()
    assert 'likes_count' in posts[0].keys()
    assert 'pk' in posts[0].keys()
    assert 'tag' in posts[0].keys()


def test_get_posts_by_username():
    post = get_posts_by_username('leo')
    assert post[0].get('poster_name') == 'leo'


def test_get_comments_by_post_id():
    post_id = 1
    comments = get_comments_by_post_id(post_id)
    assert len(comments) == 4


def test_search_for_posts():
    word = 'пирог'
    post = search_for_posts(word)
    assert word in post[0].get('content')


def test_get_post_by_pk():
    post = get_post_by_pk(1)
    assert post.get('pk') == 1
