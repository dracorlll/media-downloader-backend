from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.defaultapp.services.proxy import get_random_proxy
from apps.lib.providers.video_provider import VideoProvider


class YoutubeView(APIView):

    permission_classes = (permissions.AllowAny,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        max_try = 5
        proxy = get_random_proxy()
        url = request.data.get('url')
        source_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')

        while max_try > 0 and proxy:

            provider = VideoProvider(proxy, source_address)
            func = provider.get_video_provider(url)

            thumbnail, title, video = None, None, None

            try:
                thumbnail, title, video = func(url)
            except:
                proxy.delete()
                proxy = get_random_proxy()
                print 'Unable to download url info'

            if video:
                return Response({"data": video, "title": title, "thumbnail": thumbnail, "status": "success"})
        return Response({"status": "fail"})
