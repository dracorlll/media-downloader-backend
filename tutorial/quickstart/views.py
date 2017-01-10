from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from youtube_dl import YoutubeDL
import re


class YoutubeView(APIView):


    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    parser_classes = (JSONParser,)

    def get(self, request,  *args, **kwargs):
        return Response({"success": True})

    def post(self, request, format=None):
        url = request.data.get('url', None)
        regex = r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$'
        # quality = request.data.get('quality', None)
        if re.match(regex, str(url)):
            shared_url = share_url(url)
            return Response({"success": True,
                             "url": shared_url
                             })
        else:
            return Response({"success": False})


def share_url(self):
    url = ""
    ydl = YoutubeDL()
    r = ydl.extract_info(self, download=False)
    for formats in r['formats']:
        if formats['format_id'] == '18':
            url = formats['url']
    return url
