from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


class TestRegister:
    """ Тесты регистрации """

    def test_register_endpoint_is_available(self):
        """ Тест доступности конечной точки для регистрации """

        # Гал отправляет post-запрос по адресу регистрации
        response = client.post('/auth/register/')

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
        response = client.post('/auth/register/', json=user_data)

        # Гал видит, что запрос отработал успешно
        assert response.status_code == 200

        # Гал получает json-ответ
        json_response = response.json()
        assert json_response is not None

        # В ответе Гал видит, что он получил id.
        assert 'id' in json_response

        # При этом, кроме id в json-ответе присутствует его username
        assert json_response['username'] == user_data['username']
