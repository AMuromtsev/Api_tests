import requests
import pytest
import cerberus


def test_get_dog_seo_list_all_beeds():  # самый простой get с проверкой статус == 200
    response = requests.get('https://dog.ceo/api/breeds/list/all')

    response.raise_for_status()

    print(response.json()['message'])
    assert response.status_code == 200  #


@pytest.mark.parametrize('code',
                         [200])  # единственный параметр, который мы задаём - это код, с которым будем сравнивать
def test_get_dog_seo_breed_image(request_method, breed,
                                 code):  # получаем картинку собачки по породам (на выбор akita, beagle, borzoi)
    target = 'https://dog.ceo/api/breed/' + (breed) + '/images/random'
    response = request_method(url=target)
    assert target == 'https://dog.ceo/api/breed/' + (breed) + '/images/random'
    assert response.status_code == code  # здесь сравниваем с кодом, переданным в параметрах


@pytest.mark.parametrize('code', [200])  # валидация json + проверяем элемент из json на status ==  success
def test_get_dog_seo_json_validation(base_url_dogs, request_method, code):
    target = base_url_dogs + 'breeds/image/random'
    response = request_method(url=target)
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize('code', [200])
@pytest.mark.parametrize('breeds_num', [1,3,49,50, pytest.param(51, marks=pytest.mark.xfail(reason='51>50'))])
def test_get_dog_seo_json_validation_multiple_breeds(base_url_dogs, request_method, code, breeds_num):
    target = base_url_dogs + 'breeds/image/random/' + str(breeds_num)
    response = request_method(url=target)
    breed_len = response.json()['message']

    assert len(breed_len) == breeds_num  # проверяем, что API вернул ровно столько фотографий,
    # сколько мы запросили в параметре breeds_num
    assert response.status_code == code

@pytest.mark.parametrize('breeds', ['akita','beagle','bluetick', 'borzoi'])        #получение картинок по породе собачки
@pytest.mark.parametrize('code', [200])
def test_get_dog_seo_by_breed(breeds, code,base_url_dogs,request_method):
    target = base_url_dogs + 'breed/'+ breeds+'/images/random'
    response = request_method(url=target)
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    assert response.status_code == code
    assert v.validate(response.json(), schema)
    assert response.json()['status'] == 'success'