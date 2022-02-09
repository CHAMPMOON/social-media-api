from app.settings import settings
from app import schemas
from .database import client, session
import pytest
from jose import jwt


@pytest.fixture
def test_user(client):
    user_data = {
        'email': 'world123@gmail.com',
        'password': 'password123'
    }
    res = client.post('/users/', json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']

    return new_user


def test_create_user(client):
    res = client.post(
        '/users/',
        json={
            'email': 'hello123@gmail.com',
            'password': 'password123'
        }
    )
    new_user = schemas.UserOut(**res.json())

    assert new_user.email == 'hello123@gmail.com'
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post(
        '/login',
        data={
            'username': test_user['email'],
            'password': test_user['password']
        }
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(
        login_res.access_token,
        settings.secret_key,
        algorithms=[settings.algorithm]
    )
    id = payload.get('user_id')

    assert res.status_code == 200
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
