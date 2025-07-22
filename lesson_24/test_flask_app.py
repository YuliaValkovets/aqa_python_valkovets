import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging


BASE_URL = 'http://127.0.0.1:8080'
USERNAME = 'test_user'
PASSWORD = 'test_pass'

# Logger settings
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('test_search.log')

console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


@pytest.fixture(scope='class')
def authorization(request):
    session = requests.Session()
    resp = session.post(f'{BASE_URL}/auth', auth=HTTPBasicAuth(USERNAME,PASSWORD))
    token = resp.json().get('access_token')
    session.headers.update({'Authorization': 'Bearer ' + token})
    request.cls.session = session

    yield session

    session.close()

@pytest.mark.usefixtures('authorization')
class TestCarsAPISearch:

    @pytest.mark.parametrize('sort_by, limit', [
                             ('brand', 1 ),
                             ('year', 25),
                             ('engine_volume', 12),
                             ('price', 2),
                             (None, 24),
                             ('year', None),
                             (None, None)])

    def test_search_cars(self, sort_by, limit, request):

        params = {}
        if sort_by:
            params['sort_by'] = sort_by
        if limit is not None:
            params['limit'] = limit

        logger.info(f'\n***Test: {request.node.name}***')
        logger.info(f'GET {BASE_URL}/cars?{params}')

        response = self.session.get(f'{BASE_URL}/cars', params=params)

        logger.info(f'Status code: {response.status_code}')
        assert response.status_code == 200

        cars_data = response.json()
        logger.info(f'Number of cars: {len(cars_data)}')

        if limit is not None:
            assert len(cars_data) <= int(limit)

        if sort_by:
            cars_values = [car[sort_by] for car in cars_data]
            assert cars_values == sorted(cars_values)
