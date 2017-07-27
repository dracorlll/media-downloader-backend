from json import loads
from apps.defaultapp.serializers import proxy
from apps.defaultapp.models import Proxy
from apps.lib.clients.gimmeproxy_client import GimmeProxy
from django.core import serializers


def new_proxy():
    content, body = GimmeProxy.get_proxy()
    if content.get('status') == '200':
        response_body = loads(body)
        proxies = response_body.get('data').get('proxies')
        for proxi in proxies:
            Proxy.objects.get_or_create(ip=proxi, ttl=0)
    return None


def get_random_proxy():
    proxies = Proxy.objects.values('ip', 'id', 'ttl').filter(ttl__lt=2)[:1]
    if proxies:
        id_ = proxies[0]['id']
        ttl_ = proxies[0]['ttl'] + 1
        Proxy.objects.all().filter(id=id_).update(ttl=ttl_)
        return proxies[0]['ip']
    else:
        Proxy.objects.all().update(ttl=0)
        proxies = Proxy.objects.values('ip', 'id', 'ttl').filter(ttl__lt=2)[:1]
        id_ = proxies[0]['id']
        ttl_ = proxies[0]['ttl'] + 1
        Proxy.objects.all().filter(id=id_).update(ttl=ttl_)
        return proxies[0]['ip']
