from itertools import cycle
from typing import List, Optional

from config import config

class ProxyDispatcher:
    proxies: Optional[List[str]] = None

    def __init__(self, proxy_file: Optional[str] = None) -> None:
        if proxy_file is None or proxy_file == '':
            return

        with open(proxy_file, 'r') as file:
            self.proxies = file.read().splitlines()

        self.proxy_cycle = cycle(self.proxies)

    def get_proxy(self) -> Optional[str]:
        if self.proxies is None:
            return None

        return next(self.proxy_cycle)

proxy_dispatcher = ProxyDispatcher(config.PROXY_FILE)
