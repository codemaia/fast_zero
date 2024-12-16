from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange(organizacao)

    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # assert (garantir)
    assert response.json() == {'message': 'Hello World!'}  # Assert


def test_create_user(
    client,
):  # O parametri passado é uma Fixture https://www.youtube.com/watch?v=sidi9Z_IkLU
    # client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'livia',
            'email': 'livia@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'livia',
        'email': 'livia@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'livia',
                'email': 'livia@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'renan atualizado',
            'email': 'renan@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'renan atualizado',
        'email': 'renan@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
