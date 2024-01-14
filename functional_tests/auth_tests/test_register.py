import pytest


register_url = '/auth/register/'


@pytest.mark.asyncio(scope="session")
@pytest.mark.usefixtures('db_clear', 'db_init')
class TestRegister:
    """ Тесты регистрации """

    async def test_register_endpoint_is_available(self, client):
        """ Тест доступности конечной точки для регистрации """

        # Гал отправляет post-запрос по адресу регистрации
        response = await client.post(register_url)

        # И видит, что эта точка существует
        assert response.status_code != 404

    async def test_can_register(self,
                                client,
                                gal_data):
        """ Тест возможности регистрации """

        # Гал хочет зарегистрировать с данными из gal_data
        # Он отправляет эти данные на конечную точку регистрации
        response = await client.post(register_url, json=gal_data)

        # Гал видит, что запрос отработал успешно
        assert response.status_code == 200

        # Гал получает json-ответ
        json_response = response.json()
        assert json_response is not None

        # В ответе Гал видит, что он получил id.
        assert 'id' in json_response

        # При этом, кроме id в json-ответе присутствует его username
        assert json_response['username'] == gal_data['username']

    async def test_different_users_have_different_id(self,
                                                     client,
                                                     gal_data,
                                                     shaitan_data):
        """ Тест, проверяющий, что id разных пользователей разный """

        # Гал и Шайтан хотят зарегистрироваться
        # Они имеют два набора данных gal_data и shaitan_data

        # Сначала Гал отправляет свои данные для регистрации
        response = await client.post(register_url, json=gal_data)

        # Из ответа Гал запоминает свой id
        id_gal = response.json().get('id')

        # Потом Шайтан отправляет свои данные
        response = await client.post(register_url, json=shaitan_data)

        # И запоминает свой id
        id_shaitan = response.json().get('id')

        # Ребята понимают, что их id не должны быть одинаковыми
        assert id_gal != id_shaitan
