import subprocess
import signal
import requests
import atexit
import time


class Onion(object):
    _instance = None
    proxies = {'http': 'socks5://127.0.0.1:9050',
               'https': 'socks5://127.0.0.1:9050'}
    proc = subprocess.Popen('tor', stdout=subprocess.DEVNULL)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            atexit.register(cls._instance.stop)

        return cls._instance

    def restart(self):
        self.stop()
        self.proc = subprocess.Popen('tor', stdout=subprocess.DEVNULL)
        time.sleep(5)

    def stop(self):
        self.proc.kill()


def request(url):
    onion = Onion()
    res = requests.get(url, proxies=onion.proxies)
    return res


def request_each(urls, step=5):
    onion = Onion()
    loop_count = 0
    result = []
    for url in urls:
        result.append(request(url))
        loop_count += 1

        if loop_count == step:
            onion.restart()
            loop_count = 0
