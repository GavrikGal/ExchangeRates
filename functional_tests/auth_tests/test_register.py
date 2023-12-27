from fastapi.testclient import TestClient
from main import app


register_url = '/auth/register/'
client = TestClient(app)


class TestRegister:
    """ Тесты регистрации """

    def test_register_endpoint_is_available(self):
        """ Тест доступности конечной точки для регистрации """

        # Гал отправляет post-запрос по адресу регистрации
        response = client.post(register_url)

        # И видит, что эта точка существует
        assert response.status_code != 404

    def test_can_register(self):
        """ Тест возможности регистрации """

        # Гал хочет зарегистрировать со следующими данными
        user_data = {
            'username': 'test_gal',
            'password': 'test_password'
        }

        # Он отправляет эти данные на конечную точку регистрации
        response = client.post(register_url, json=user_data)

        # Гал видит, что запрос отработал успешно
        assert response.status_code == 200

        # Гал получает json-ответ
        json_response = response.json()
        assert json_response is not None

        # В ответе Гал видит, что он получил id.
        assert 'id' in json_response

        # При этом, кроме id в json-ответе присутствует его username
        assert json_response['username'] == user_data['username']

    def test_different_users_have_different_id(self):
        """ Тест, проверяющий, что id разных пользователей разный """

        # Гал и Шайтан хотят зарегистрироваться
        # Они имеют два набора данных
        user1_data = {
            'username': 'test_gal',
            'password': 'test_password'
        }
        user2_data = {
            'username': 'test_shaitan',
            'password': 'test_password'
        }

        # Сначала Гал отправляет свои данные для регистрации
        response = client.post(register_url, json=user1_data)

        # Из ответа Гал запоминает свой id
        id_gal = response.json().get('id')

        # Потом Шайтан отправляет свои данные
        response = client.post(register_url, json=user2_data)

        # И запоминает свой id
        id_shaitan = response.json().get('id')

        # Ребята понимают, что их id не должны быть одинаковыми
        assert id_gal != id_shaitan
