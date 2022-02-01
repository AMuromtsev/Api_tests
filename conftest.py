import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        '--breed',
        default='akita',
        help='Это порода собаки, на выбор доступна для тестов Акита, Бигль или Борзая. По умолчанию - Акита',
        choices = ['akita', 'beagle', 'borzoi']
    )

    parser.addoption (
        '--method',
        default = 'get',
        help = 'Выбор метода для обращения к API',
        choices = ['get', 'post', 'put', 'delete', 'patch']

    )
    parser.addoption(
        '--base_url_dogs',
        default = 'https://dog.ceo/api/',
        help='базовый url для API с собачками'
    )

    parser.addoption(
        '--breeds_num',
        default=3,
        help='количество картинок с собаками, которые можно запросить',
        choices = [range(1,50)]
    )

    parser.addoption(
        '--base_url_brewery',
        default='https://api.openbrewerydb.org/',
        help='базовый url для API с openbreweby'
    )
    parser.addoption(
        '--base_url_jsonplaceholder',
        default='https://jsonplaceholder.typicode.com/',
        help='базовый url для API с jsonplaceholder'
    )

    parser.addoption(
        '--base_url_test_module',
        default='https://ya.ru',
        help='базовый url для тестового модуля'
    )

    parser.addoption(
        '--status_code',
        default=200,
        help='возможные ответы от серверов',
        choices = [200,201,300,400,404,500,502]
    )

@pytest.fixture
def breed(request):
    return request.config.getoption('--breed')

@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption('--method'))

@pytest.fixture
def base_url_dogs(request):
    return request.config.getoption('--base_url_dogs')

@pytest.fixture
def breeds_num(request):
    return request.config.getoption('--breeds_num')

@pytest.fixture
def base_url_brewery(request):
    return request.config.getoption('--base_url_brewery')

@pytest.fixture
def base_url_jsonplaceholder(request):
    return request.config.getoption('--base_url_jsonplaceholder')

@pytest.fixture
def base_url_test_module(request):
    return request.config.getoption('--base_url_test_module')

@pytest.fixture
def status_code(request):
    return request.config.getoption('--status_code')


