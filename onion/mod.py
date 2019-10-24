import subprocess
import signal
import requests


class Onion(object):
    _instance = None
    proxies = {'http': 'socks5://127.0.0.1:9050',
               'https': 'socks5://127.0.0.1:9050'}
    proc = subprocess.Popen('tor', stdout=subprocess.DEVNULL)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def restart(self):
        self.stop()
        self.proc = subprocess.Popen('tor', stdout=subprocess.DEVNULL)

    def stop(self):
        self.proc.kill()


def request(url):
    onion = Onion()
    res = requests.get(url, proxies=onion.proxies)
    onion.stop()
    return res
