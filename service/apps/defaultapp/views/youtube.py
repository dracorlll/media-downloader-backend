from django.conf import settings
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.lib.providers.video_provider import yt, vk, fb, dm, ru, vimeo
import re


class YoutubeView(APIView):

    permission_classes = (permissions.AllowAny,)
    parser_classes = (JSONParser,)

    def get(self, request,  *args, **kwargs):
        return Response({"success": True})

    def post(self, request, format=None):
        url = request.data.get('url')
        if re.match(settings.REGEX_YT, str(url)):
            thumbnail, title, video = yt(url)
            return Response({"data": video, "title": title, "thumbnail": thumbnail, "success": True})
        elif re.match(settings.REGEX_VK, str(url)):
            thumbnail, title, video = vk(url)
            return Response({"data": video, "title": title, "thumbnail": thumbnail, "success": True})
        elif re.match(settings.REGEX_FB, str(url)):
            thumbnail, title, video = fb(url)
            return Response({"data": video, "title": title, "thumbnail": thumbnail, "success": True})
        elif re.match(settings.REGEX_DM, str(url)):
            thumbnail, title, video = dm(url)
            return Response({"data": video, "title": title, "thumbnail": thumbnail, "success": True})
        elif re.search(settings.REGEX_RU, str(url)):
            thumbnail, title, video = ru(url)
            return Response({"data": video, "title": title, "thumbnail": thumbnail, "success": True})
        elif re.search(settings.REGEX_VIMEO, str(url)):
            thumbnail, title, video = vimeo(url)
            return Response({"data": video, "title": title, "thumbnail": thumbnail, "success": True})
        else:
            return Response({'success': False})
