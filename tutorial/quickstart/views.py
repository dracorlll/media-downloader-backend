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
        regex_yt = r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$'
        regex_vk = r'^((?:https?:)?\/\/)?((?:www)\.)?((?:vk.com))'
        regex_fb = r'^((https|http):\/\/(www|m).facebook.com)'
        regex_dm = r'^((http|https):\/\/(www|m).dailymotion.com)'
        regex_ru = r'(?:^|\W)mail.ru(?:$|\W)'
        if re.match(regex_yt, str(url)):
            title, video = yt_url(url)
            return Response({
                             "data": video,
                             "title": title,
                             "success": True,
                             })
        elif re.match(regex_vk, str(url)):
            title, video = vk_url(url)
            return Response({
                "data": video,
                "title": title,
                "success": True,
            })
        # elif re.match(regex_fb, str(url)):
        #     title, video = fb_url(url)
        #     return Response({
        #         "data": video,
        #         "title": title,
        #         "success": True,
        #     })
        elif re.match(regex_dm, str(url)):
            title, video = dm_url(url)
            return Response({
                "data": video,
                "title": title,
                "success": True,
            })
        elif re.search(regex_ru, str(url)):
            title, video = ru_url(url)
            return Response({
                "data": video,
                "title": title,
                "success": True,
            })
        else:
            # return Response({"success": False})
            ydl = YoutubeDL()
            r = ydl.extract_info(url, download=False)
            return Response({
                "data": r
            })


def yt_url(self):
    ydl = YoutubeDL()
    video = {}
    r = ydl.extract_info(self, download=False)
    title = r['title']
    for formats in r['formats']:
        if (formats['format_id'] == '18') or (formats['format_id'] == '140') or (formats['format_id'] == '22'):
            url = formats['url']
            ext = formats['ext']
            liste = {'url': url, 'ext': ext}
            video[formats['format_id']] = liste
    return title, video


def vk_url(self):
    url = re.split(r'((?:video-?)[0-9]+_[0-9]+)', str(self))
    video = {}
    title = url[1]
    video[0] = {'url': "https://vk.com/" + url[1], 'ext': 'mp4'}
    return title, video


def fb_url(self):
    ydl = YoutubeDL()
    video = {}
    r = ydl.extract_info(self, download=False)
    title = r['title']
    for formats in r['formats']:
        if formats['format_id'] == 'dash_hd_src_no_ratelimit':
            url = formats['url']
            ext = formats['ext']
            liste = {'url': url, 'ext': ext}
            video[formats['format_id']] = liste
    return title, video


def dm_url(self):
    ydl = YoutubeDL()
    video = {}
    r = ydl.extract_info(self, download=False)
    title = r['title']
    for formats in r['formats']:
        if (formats['format_id'] == 'http-380') or (formats['format_id'] == 'http-480') or (formats['format_id'] == 'http-240') or (formats['format_id'] == 'http-720') or (formats['format_id'] == 'http-1080') or (formats['format_id'] == 'http-360'):
            url = formats['url']
            ext = formats['ext']
            liste = {'url': url, 'ext': ext}
            video[formats['format_id']] = liste
    return title, video


def ru_url(self):
    ydl = YoutubeDL()
    video = {}
    r = ydl.extract_info(self, download=False)
    title = r['title']
    for formats in r['formats']:
        if (formats['format_id'] == '360p') or (formats['format_id'] == '240p') or (formats['format_id'] == '480p') or (formats['format_id'] == '720p') or (formats['format_id'] == '1080p'):
            url = formats['url']
            ext = formats['ext']
            liste = {'url': url, 'ext': ext}
            video[formats['format_id']] = liste
    return title, video
