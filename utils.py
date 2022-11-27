import json


def load_posts():
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def load_comments():
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments = json.load(file)
    return comments


def get_posts_by_username(user_name):
    posts = load_posts()
    user_posts = []
    for post in posts:
        if post.get('poster_name') == user_name:
            user_posts.append(post)
    if len(user_posts) == 0:
        raise ValueError('Такого пользователя не существует или у него нет постов')
    return user_posts


def get_comments_by_post_id(post_id):
    comments = load_comments()
    comments_for_post_id = []
    count = 0
    for comment in comments:
        if comment.get('post_id') == post_id:
            count += 1
            comments_for_post_id.append(comment)
    if count == 0:
        raise ValueError('Такого поста нет')
    return comments_for_post_id


def search_for_posts(query):
    posts = load_posts()
    posts_for_query = []
    for post in posts:
        if query.lower() in post.get('content').lower():
            posts_for_query.append(post)
    return posts_for_query


def get_post_by_pk(pk):
    posts = load_posts()
    for post in posts:
        if post.get('pk') == pk:
            post_by_pk = post
    return post_by_pk


def get_posts_by_tag(tag):
    posts = load_posts()
    posts_with_tag = []
    for post in posts:
        if tag in post.get('tag'):
            posts_with_tag.append(post)
    return posts_with_tag


def load_bookmarks():
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)
        return bookmarks


def add_bookmark(post_id):
    bookmarks = load_bookmarks()
    post = get_post_by_pk(post_id)
    bookmarks.append(post)
    save_bookmarks(bookmarks)


def save_bookmarks(bookmarks):
    with open('data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file, ensure_ascii=False)


def delete_bookmark(bookmark_id):
    bookmarks = load_bookmarks()
    for index, bookmark in enumerate(bookmarks):
        if bookmark.get('pk') == bookmark_id:
            del bookmarks[index]
            break
    save_bookmarks(bookmarks)
