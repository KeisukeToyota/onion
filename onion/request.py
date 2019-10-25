import requests
from onion.onion import Onion


def get(url):
    onion = Onion()
    res = requests.get(url, proxies=onion.proxies)
    return res


def post(url, params=None):
    onion = Onion()
    res = requests.post(url, params=params)
    return res
