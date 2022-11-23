from main import app

def test_api_posts():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list
    assert 'poster_name' in response.json[0].keys()
    assert 'poster_avatar' in response.json[0].keys()
    assert 'pic' in response.json[0].keys()
    assert 'content' in response.json[0].keys()
    assert 'views_count' in response.json[0].keys()
    assert 'likes_count' in response.json[0].keys()
    assert 'pk' in response.json[0].keys()
    assert 'tag' in response.json[0].keys()


def test_api_for_post_id():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict
    assert 'poster_name' in response.json.keys()
    assert 'poster_avatar' in response.json.keys()
    assert 'pic' in response.json.keys()
    assert 'content' in response.json.keys()
    assert 'views_count' in response.json.keys()
    assert 'likes_count' in response.json.keys()
    assert 'pk' in response.json.keys()
    assert 'tag' in response.json.keys()
