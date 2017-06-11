import json
import httplib2
import urllib


class HttpClient:
    def __init__(self):
        pass

    @classmethod
    def post_audio(cls, uri, data, headers=None):
        return HttpClient.__request(uri, "POST", data, headers)

    @classmethod
    def get_connection(cls):
        return httplib2.Http()

    @classmethod
    def get(cls, uri, query_params=None, headers=None):
        if query_params:
            uri += '?%s' % urllib.urlencode(query_params)
        return HttpClient.__request(uri, "GET", None, headers=headers)

    @classmethod
    def post(cls, uri, data=json.dumps({}), headers=None):
        return HttpClient.__request(uri, "POST", data, headers=headers)

    @classmethod
    def put(cls, uri, data=json.dumps({}), headers=None):
        return HttpClient.__request(uri, "PUT", data, headers=headers)

    @classmethod
    def delete(cls, uri, headers=None):
        return HttpClient.__request(uri, "DELETE", None, headers=headers)

    @classmethod
    def proxy(cls, url, method, data=None, headers=None):
        return HttpClient.__request(url, method, data, headers)

    @classmethod
    def __request(cls, url, method, data=None, headers=None):
        if not isinstance(data, basestring):
            data = json.dumps(data) if data is not None else data
        return HttpClient.get_connection().request(url, method, body=data, headers=headers)
