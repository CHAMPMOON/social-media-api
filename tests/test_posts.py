import pytest
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get('/posts/')

    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200


def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get('/posts/')

    assert res.status_code == 401


def test_get_one_post(client, test_posts):
    res = client.get(f'/posts/{test_posts[0].id}')
    post = schemas.PostOut(**res.json())

    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title


def test_get_one_post_not_exist(client, test_posts):
    res = client.get('/posts/12345')

    assert res.status_code == 404


@pytest.mark.parametrize('title, content, published', [
    ('best phone', 'some random text', True),
    ('best TV', 'hello world', False),
    ('i miss you', 'you is not my', True),
])
def test_create_post(
    authorized_client, test_user, test_posts,
    title, content, published
):
    res = authorized_client.post(
        '/posts/',
        json={
            'title': title,
            'content': content,
            'published': published
        }
    )
    created_post = schemas.Post(**res.json())

    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user['id']


def test_create_post_default_publiched_true(
    authorized_client, test_user, test_posts
):
    res = authorized_client.post(
        '/posts/',
        json={
            'title': 'test_title_1',
            'content': 'abcdef'
        }
    )
    created_post = schemas.Post(**res.json())

    assert res.status_code == 201
    assert created_post.title == 'test_title_1'
    assert created_post.content == 'abcdef'
    assert created_post.published is True
    assert created_post.owner_id == test_user['id']


def test_unauthorized_user_create_posts(client, test_posts, test_user):
    res = client.post(
        '/posts/',
        json={
            'title': 'random title',
            'content': 'random some'
        }
    )
    assert res.status_code == 401


def test_unauthorized_user_delete_posts(client, test_posts, test_user):
    res = client.delete(
        f'/posts/{test_posts[0].id}',
    )
    assert res.status_code == 401


def test_authorized_user_delete_posts(
    authorized_client, test_posts, test_user
):
    res = authorized_client.delete(
        f'/posts/{test_posts[0].id}',
    )
    assert res.status_code == 204


def test_delete_post_non_exist(
    authorized_client, test_posts, test_user
):
    res = authorized_client.delete('/posts/12345')

    assert res.status_code == 404


def test_delete_other_user_post(
    authorized_client, test_posts, test_user
):
    res = authorized_client.delete(
        f'/posts/{test_posts[3].id}'
    )
    assert res.status_code == 403


def test_authorized_update_post(
    authorized_client, test_posts, test_user
):
    data = {
        'title': 'updated title',
        'content': 'updated content',
        'id': test_posts[0].id
    }
    res = authorized_client.put(
        f'/posts/{test_posts[0].id}',
        json=data
    )
    updated_post = schemas.Post(**res.json())

    assert res.status_code == 200
    assert updated_post.title == data['title']
    assert updated_post.content == data['content']
    assert updated_post.id == data['id']


def test_unauthorized_update_post(
    client, test_posts, test_user
):
    res = client.put(
        f'/posts/{test_posts[0].id}'
    )
    assert res.status_code == 401


def test_update_other_user_post(
    authorized_client, test_posts, test_user
):
    data = {
        'title': 'updated title',
        'content': 'updated content',
        'id': test_posts[0].id
    }
    res = authorized_client.put(
        f'/posts/{test_posts[3].id}',
        json=data
    )
    assert res.status_code == 403


def test_update_post_non_exist(
    authorized_client, test_posts, test_user
):
    data = {
        'title': 'updated title',
        'content': 'updated content',
        'id': test_posts[0].id
    }
    res = authorized_client.put(
        '/posts/12345',
        json=data
    )
    assert res.status_code == 404
