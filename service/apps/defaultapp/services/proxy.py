from json import loads
from random import randint
from datetime import datetime, timedelta

from django.conf import settings

from apps.defaultapp.models import Proxy
from apps.lib.clients.gimmeproxy_client import GimmeProxy


def new_proxy():
    proxy = None
    content, body = GimmeProxy.get_proxy()
    if content.get('status') == '200':
        response_body = loads(body)
        print response_body.get('data')
        defaults = {
            'ip': '0'
        }
        proxy = None
    return proxy


def get_random_proxy():
    count = Proxy.objects.count()
    random_index = randint(0, count - 1)
    proxies = Proxy.objects.all()
    if proxies:
        return proxies[random_index]
    return None


def clean_proxy_list():
    proxies = Proxy.objects.all()

    for proxy in proxies:
        tz = proxy.timestamp.tzinfo
        delta = datetime.now(tz) - proxy.timestamp
        max_life = timedelta(minutes=settings.MAX_PROXY_LIFE)
        if delta > max_life:
            proxy.delete()
