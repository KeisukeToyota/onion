import requests
from requests.models import Response 
from onion.onion import Onion


def get(url: str, headers=None, params=None) -> Response:
    onion = Onion()
    res = requests.get(url, headers=headers, params=params, proxies=onion.proxies)
    return res


def post(url: str, headers=None, params=None) -> Response:
    onion = Onion()
    res = requests.post(url, headers=headers, params=params, proxies=onion.proxies)
    return res


def put(url: str, headers=None, params=None) -> Response:
    onion = Onion()
    res = requests.put(url, headers=headers, params=params, proxies=onion.proxies)
    return res


def delete(url: str, headers=None, params=None) -> Response:
    onion = Onion()
    res = requests.delete(url, headers=headers, params=params, proxies=onion.proxies)
    return res
