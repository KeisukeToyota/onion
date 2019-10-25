import subprocess
import atexit
import time


class Onion(object):
    _instance = None
    proc = None
    proxies = {'http': 'socks5://127.0.0.1:9050',
               'https': 'socks5://127.0.0.1:9050'}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.start()
            atexit.register(cls._instance.stop)

        return cls._instance

    def restart(self):
        self.stop()
        self.proc = subprocess.Popen('tor', stdout=subprocess.DEVNULL)
        time.sleep(5)

    def stop(self):
        self.proc.kill()

    def start(self):
        self.proc = subprocess.Popen('tor', stdout=subprocess.DEVNULL)
