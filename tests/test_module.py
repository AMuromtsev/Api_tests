import requests
import pytest

def test_module_request(base_url_test_module,status_code, request_method):
    target = base_url_test_module
    response = request_method(url = target)
    assert response.status_code == status_code
