import re
from django.conf import settings
from youtube_dl import YoutubeDL


class VideoProvider:

    ydl = None

    def __init__(self, proxy):
        if proxy:
            self.ydl = YoutubeDL(params={'proxy': str(proxy), 'socket_timeout': '5'})
            print 'Using proxy ' + str(proxy)
        else:
            self.ydl = YoutubeDL(params={'socket_timeout': '10'})
            print 'Not using proxy'

    def other(self, url):
        url = self.ydl.extract_info(url, download=False)
        format_id = str(url.get('format', 'best')).split(' ').__getitem__(0)
        video = []
        title = url['title']
        thumbnail = url['thumbnails'][0]['url']
        if format_id:
            for formats in url['formats']:
                if formats['format_id'] == format_id:
                    url = formats['url']
                    ext = formats['ext']
                    format_id = 'best'
                    try:
                        filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                    except:
                        filesize = None
                    liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
                    video.append(liste)
        else:
            for formats in url['formats']:
                url = formats['url']
                ext = formats['ext']
                format_id = formats['format_id']
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
                video.append(liste)
        return thumbnail, title, video

    def vimeo(self, url):
        regex = r'(http-)'
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        print self.ydl.list_formats(r)
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if re.search(regex, formats['format_id']):
                url = formats['url']
                ext = formats['ext']
                format_id = str(formats['format_id']).split('-').__getitem__(1)
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
                video.append(liste)
        return thumbnail, title, video

    def yt(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if (formats['format_id'] == '18') or (formats['format_id'] == '140') or (formats['format_id'] == '22'):
                url = formats['url']
                ext = formats['ext']
                if formats['format_id'] != '140':
                    format_id = str(formats['height']) + 'p'
                else:
                    format_id = "audio"
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste)

        return thumbnail, title, video

    def vk(self, url):
        regex = r'(cache)'
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if re.match(regex, formats['format_id']):
                url = formats['url']
                ext = formats['ext']
                format_id = formats['format_id']
                print format_id
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
                video.append(liste)
        return thumbnail, title, video

    def ins(self, url):
        regex = r'(0)'
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if re.match(regex, formats['format_id']):
                url = formats['url']
                ext = formats['ext']
                format_id = formats['format_id']
                print format_id
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
                video.append(liste)
        return thumbnail, title, video

    def fb(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if formats['format_id'] == 'dash_hd_src_no_ratelimit':
                url = formats['url']
                ext = formats['ext']
                format_id = 'high quality'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
                video.append(liste)
            elif formats['format_id'] == 'dash_sd_src_no_ratelimit':
                url = formats['url']
                ext = formats['ext']
                format_id = 'standart quality'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
                video.append(liste)
        return thumbnail, title, video

    def dm(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if (formats['format_id'] == 'http-380') or (formats['format_id'] == 'http-480') or (
                        formats['format_id'] == 'http-240') or (formats['format_id'] == 'http-720') or (
                        formats['format_id'] == 'http-1080') or (formats['format_id'] == 'http-360'):
                url = formats['url']
                ext = formats['ext']
                format_id = str(formats['format_id']).split('-').__getitem__(1) + 'p'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
                video.append(liste)
        return thumbnail, title, video

    def ru(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if (formats['format_id'] == '360p') or (formats['format_id'] == '240p') or (
                        formats['format_id'] == '480p') or (formats['format_id'] == '720p') or (
                        formats['format_id'] == '1080p'):
                url = formats['url']
                ext = formats['ext']
                format_id = formats['format_id']
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste)
        return thumbnail, title, video

    def yahoo(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if str(formats['format_id']).split('-').__getitem__(0) == 'mp4':
                url = formats['url']
                ext = formats['ext']
                format_id = str(formats['height']) + 'p'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste)
        return thumbnail, title, video

    def breakvideo(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if str(formats['format_id']).split('-').__getitem__(0) == 'http':
                url = formats['url']
                ext = formats['ext']
                format_id = str(formats['height']) + 'p'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste)
        return thumbnail, title, video

    def flicker(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        try:
            thumbnail = r['thumbnails'][0]['url']
        except:
            thumbnail = None

        for formats in r['formats']:
            if formats['format_id'] == '700':
                url = formats['url']
                ext = formats['ext']
                format_id = 'standart'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste)
        return thumbnail, title, video

    def funny(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if str(formats['format_id']).split('-').__getitem__(0) == 'mp4':
                url = formats['url']
                ext = formats['ext']
                format_id = str(formats['height']) + 'p'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste)
        return thumbnail, title, video

    def liveleak(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if formats['format_id'] == '0' or formats['format_id'] == '1':
                url = formats['url']
                ext = formats['ext']
                if formats['height'] == None:
                    format_id = '240p'
                else:
                    format_id = str(formats['height']) + 'p'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste)
        return thumbnail, title, video

    def ted(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if str(formats['format_id']).split('-').__getitem__(0) == 'http':
                url = formats['url']
                ext = formats['ext']
                format_id = str(formats['height']) + 'p'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste),
        return thumbnail, title, video

    def twitch(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if formats['format_id'] == 'Audio_Only' or 'Source':
                url = formats['url']
                ext = formats['ext']
                format_id = formats['format_id']
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste),
            else:
                url = formats['url']
                ext = formats['ext']
                format_id = formats['format_id']
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste),
        return thumbnail, title, video

    def twitter(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if str(formats['format_id']).split('-').__getitem__(0) == 'hls':
                url = formats['url']
                ext = formats['ext']
                format_id = str(formats['height']) + 'p'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste),
        return thumbnail, title, video

    def ustream(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            url = formats['url']
            ext = formats['ext']
            format_id = 'standart'
            try:
                filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
            except:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                     'http_headers': formats['http_headers']}
            video.append(liste),

        return thumbnail, title, video

    def viewster(self, url):
        video = []
        r = self.ydl.extract_info(url, download=False)
        title = r['title']
        thumbnail = r['thumbnails'][0]['url']
        for formats in r['formats']:
            if str(formats['format_id']).split('-').__getitem__(0) == 'hls':
                url = formats['url']
                ext = formats['ext']
                format_id = str(formats['height']) + 'p'
                try:
                    filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
                except:
                    filesize = None
                liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id,
                         'http_headers': formats['http_headers']}
                video.append(liste),
        return thumbnail, title, video

    def get_video_provider(self, url):
        func = None
        if re.match(settings.REGEX_YT, str(url)):
            func = self.yt
        elif re.match(settings.REGEX_VK, str(url)):
            func = self.vk
        elif re.match(settings.REGEX_FB, str(url)):
            func = self.fb
        elif re.match(settings.REGEX_DM, str(url)):
            func = self.dm
        elif re.search(settings.REGEX_RU, str(url)):
            func = self.ru
        elif re.search(settings.REGEX_VIMEO, str(url)):
            func = self.vimeo
        elif re.search(settings.REGEX_INS, str(url)):
            func = self.ins
        elif re.search(settings.REGEX_YAHOO, str(url)):
            func = self.yahoo
        elif re.search(settings.REGEX_BREAK, str(url)):
            func = self.breakvideo
        elif re.search(settings.REGEX_FLICKER, str(url)):
            func = self.flicker
        elif re.search(settings.REGEX_FUNNY, str(url)):
            func = self.funny
        elif re.search(settings.REGEX_LIVELEAK, str(url)):
            func = self.liveleak
        elif re.search(settings.REGEX_TED, str(url)):
            func = self.ted
        elif re.search(settings.REGEX_TWITCH, str(url)):
            func = self.twitch
        elif re.search(settings.REGEX_TWITTER, str(url)):
            func = self.twitter
        elif re.search(settings.REGEX_USTREAM, str(url)):
            func = self.ustream
        elif re.search(settings.REGEX_VIEWSTER, str(url)):
            func = self.viewster
        else:
            func = self.other
        return func
