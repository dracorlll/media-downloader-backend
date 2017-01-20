from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from youtube_dl import YoutubeDL
import re
from regex_urls import *


class YoutubeView(APIView):

    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    parser_classes = (JSONParser,)

    def get(self, request,  *args, **kwargs):
        return Response({"success": True})

    def post(self, request, format=None):
        url = request.data.get('url', None)
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
        elif re.match(regex_fb, str(url)):
            title, video = fb_url(url)
            return Response({
                "data": video,
                "title": title,
                "success": True,
            })
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
        elif re.search(regex_vimeo, str(url)):
            title, video = vimeo_url(url)
            return Response({
                "data": video,
                "title": title,
                "success": True,
            })
        elif re.search(regex_url, str(url)):
            ydl = YoutubeDL()
            info_dict = ydl.extract_info(url, download=False)
            r = info_dict.get('format', 'best')
            if r.__len__() == 0:
                return Response({
                    'success': False
                })
            else:
                title, video = other_url(info_dict)
                return Response({
                    "data": video,
                    "title": title,
                    "success": True
                })
        else:
            return Response({
                'success': False
            })


def other_url(self):
    format_id = str(self.get('format', 'best')).split(' ').__getitem__(0)
    video = {}
    title = self['title']
    for formats in self['formats']:
        if formats['format_id'] == format_id:
            url = formats['url']
            ext = formats['ext']
            try:
                filesize = formats['filesize']
            except KeyError:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize}
            video['best'] = liste
    return title, video


def vimeo_url(self):
    ydl = YoutubeDL()
    regex = r'(http-)'
    video = {}
    r = ydl.extract_info(self, download=False)
    title = r['title']
    for formats in r['formats']:
        if re.search(regex, formats['format_id']):
            url = formats['url']
            ext = formats['ext']
            try:
                filesize = formats['filesize']
            except KeyError:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize}
            video[str(formats['format_id']).split('-').__getitem__(1)] = liste
    return title, video


def yt_url(self):
    ydl = YoutubeDL()
    video = {}
    r = ydl.extract_info(self, download=False)
    title = r['title']
    for formats in r['formats']:
        if (formats['format_id'] == '18') or (formats['format_id'] == '140') or (formats['format_id'] == '22'):
            url = formats['url']
            ext = formats['ext']
            try:
                filesize = formats['filesize']
            except KeyError:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize}
            if formats['format_id'] != '140':
                video[str(formats['height']) + 'p'] = liste
            else:
                video['audio'] = liste
    return title, video


def vk_url(self):
    ydl = YoutubeDL()
    regex = r'(hls-)'
    video = {}
    r = ydl.extract_info(self, download=False)
    title = r['title']
    for formats in r['formats']:
        if re.match(regex, formats['format_id']) and formats['format_id'] != 'hls-meta':
            url = formats['url']
            ext = formats['ext']
            try:
                filesize = formats['filesize']
            except KeyError:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize}
            video[str(formats['format']).split('x').__getitem__(1) + 'p'] = liste
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
            try:
                filesize = formats['filesize']
            except KeyError:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize}
            video['high quality'] = liste
        elif formats['format_id'] == 'dash_sd_src_no_ratelimit':
            url = formats['url']
            ext = formats['ext']
            try:
                filesize = formats['filesize']
            except KeyError:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize}
            video['standart quality'] = liste
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
            try:
                filesize = formats['filesize']
            except KeyError:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize}
            video[str(formats['format_id']).split('-').__getitem__(1) + 'p'] = liste
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
            try:
                filesize = formats['filesize']
            except KeyError:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize}
            video[formats['format_id']] = liste
    return title, video
