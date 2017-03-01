from django.conf import settings
from apps.lib.clients.http_client import HttpClient


class GimmeProxy:
    def __init__(self):
        pass

    @classmethod
    def get_proxy(cls):
        query_params = {
            'api_key': settings.GIMMEPROXY_API_KEY,
            'get': 'true',
            'websites': 'google',
            'maxCheckPeriod': 3600,
            'minSpeed': 50,
            'supportsHttps': True
        }
        return HttpClient.get(settings.GIMMEPROXY_BASE_URL, query_params=query_params)
