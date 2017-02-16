
# def other(url):
#     format_id = str(url.get('format', 'best')).split(' ').__getitem__(0)
#     video = []
#     title = url['title']
#     thumbnail = url['thumbnails'][0]['url']
#     if not format_id:
#         for formats in url['formats']:
#             if formats['format_id'] == format_id:
#                 url = formats['url']
#                 ext = formats['ext']
#                 format_id = 'best'
#                 try:
#                     filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
#                 except:
#                     filesize = None
#                 liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
#                 video.append(liste)
#     else:
#         for formats in url['formats']:
#             url = formats['url']
#             ext = formats['ext']
#             format_id = 'best'
#             try:
#                 filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
#             except:
#                 filesize = None
#             liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
#             video.append(liste)
#     return thumbnail, title, video
import re
from youtube_dl import YoutubeDL


def vimeo(url):
    ydl = YoutubeDL()
    regex = r'(http-)'
    video = []
    r = ydl.extract_info(url, download=False)
    title = r['title']
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


def yt(url):
    ydl = YoutubeDL()
    video = []
    r = ydl.extract_info(url, download=False)
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
                filesize = str(float("{0:.2f}".format(float(formats['filesize'])/1048576))) + ' Mb'
            except:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
            video.append(liste)

    return thumbnail, title, video


def vk(url):
    ydl = YoutubeDL()
    regex = r'(hls-)'
    video = []
    r = ydl.extract_info(url, download=False)
    title = r['title']
    thumbnail = r['thumbnails'][0]['url']
    for formats in r['formats']:
        if re.match(regex, formats['format_id']) and formats['format_id'] != 'hls-meta':
            url = formats['url']
            ext = formats['ext']
            format_id = str(formats['format']).split('x').__getitem__(1) + 'p'
            try:
                filesize = str(float("{0:.2f}".format(float(formats['filesize']) / 1048576))) + ' Mb'
            except:
                filesize = None
            liste = {'url': url, 'ext': ext, 'size': filesize, 'format': format_id}
            video.append(liste)
    return thumbnail, title, video


def fb(url):
    ydl = YoutubeDL()
    video = []
    r = ydl.extract_info(url, download=False)
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


def dm(url):
    ydl = YoutubeDL()
    video = []
    r = ydl.extract_info(url, download=False)
    title = r['title']
    thumbnail = r['thumbnails'][0]['url']
    for formats in r['formats']:
        if (formats['format_id'] == 'http-380') or (formats['format_id'] == 'http-480') or (formats['format_id'] == 'http-240') or (formats['format_id'] == 'http-720') or (formats['format_id'] == 'http-1080') or (formats['format_id'] == 'http-360'):
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


def ru(url):
    ydl = YoutubeDL()
    video = []
    r = ydl.extract_info(url, download=False)
    title = r['title']
    thumbnail = r['thumbnails'][0]['url']
    for formats in r['formats']:
        if (formats['format_id'] == '360p') or (formats['format_id'] == '240p') or (formats['format_id'] == '480p') or (formats['format_id'] == '720p') or (formats['format_id'] == '1080p'):
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
