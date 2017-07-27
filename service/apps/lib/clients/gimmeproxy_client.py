from django.conf import settings
from apps.lib.clients.http_client import HttpClient


class GimmeProxy:
    def __init__(self):
        pass

    @classmethod
    def get_proxy(cls):
        return HttpClient.get(settings.GIMMEPROXY_BASE_URL)
