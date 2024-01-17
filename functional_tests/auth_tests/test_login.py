import pytest


login_url = '/auth/login/'


@pytest.mark.asyncio(scope='session')
@pytest.mark.usefixtures('db_clear', 'db_init')
class TestLogin:
    """ Тесты логина """

    async def test_login_endpoint_is_available(self, client):
        """ Тест доступности конечной точки логина """

        # Гал отправляет post-запрос по адресу логина
        response = await client.post(login_url)

        # И видит, что эта точка существует
        assert response.status_code != 404

    async def test_can_login(self, client, gal_data, gal_in_db):
        """ Тест возможности залогиниться и получить JWT-токен """

        # Гал - зарегистрированный пользователь.
        # Он отправляет логин и пароль на адрес логина
        response = await client.post(login_url, json=gal_data)

        # Гал видит, что запрос отработал успешно
        assert response.status_code == 200

        # Гал получает json-ответ
        json_response = response.json()
        assert json_response is not None

        # И тип токена должен быть bearer
        assert json_response['token_type'] == 'bearer'

        # В ответе Гал видит, что он получил JWT-токен
        assert 'access_token' in json_response

        # Гал чувствует, что разработчик его может обманывать
        # И придумал как отличать реальный токен от ерунды
        assert len(json_response['access_token']) > 20


