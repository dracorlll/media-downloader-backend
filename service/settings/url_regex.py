REGEX_YT = r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$'

REGEX_VK = r'''(?x)
                    https?://
                        (?:
                            (?:
                                (?:(?:m|new)\.)?vk\.com/video_|
                                (?:www\.)?daxab.com/
                            )
                            ext\.php\?(?P<embed_query>.*?\boid=(?P<oid>-?\d+).*?\bid=(?P<id>\d+).*)|
                            (?:
                                (?:(?:m|new)\.)?vk\.com/(?:.+?\?.*?z=)?video|
                                (?:www\.)?daxab.com/embed/
                            )
                            (?P<videoid>-?\d+_\d+)(?:.*\blist=(?P<list_id>[\da-f]+))?
                        )
                    '''

REGEX_FB = r'''(?x)
                (?:
                    https?://
                        (?:[\w-]+\.)?(?:facebook\.com|facebookcorewwwi\.onion)/
                        (?:[^#]*?\#!/)?
                        (?:
                            (?:
                                video/video\.php|
                                photo\.php|
                                video\.php|
                                video/embed|
                                story\.php
                            )\?(?:.*?)(?:v|video_id|story_fbid)=|
                            [^/]+/videos/(?:[^/]+/)?|
                            [^/]+/posts/|
                            groups/[^/]+/permalink/
                        )|
                    facebook:
                )
                (?P<id>[0-9]+)
                '''

REGEX_DM = r'(?i)(?:https?://)?(?:(www|touch)\.)?dailymotion\.[a-z]{2,3}/(?:(?:embed|swf|#)/)?video/(?P<id>[^/?_]+)'

REGEX_RU = r'https?://(?:(?:www|m)\.)?my\.mail\.ru/(?:video/.*#video=/?(?P<idv1>(?:[^/]+/){3}\d+)|(?:(?P<idv2prefix>(?:[^/]+/){2})video/(?P<idv2suffix>[^/]+/\d+))\.html)'

REGEX_URL = r'[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'

REGEX_VIMEO = r'''(?x)
                    https?://
                        (?:
                            (?:
                                www|
                                (?P<player>player)
                            )
                            \.
                        )?
                        vimeo(?P<pro>pro)?\.com/
                        (?!(?:channels|album)/[^/?#]+/?(?:$|[?#])|[^/]+/review/|ondemand/)
                        (?:.*?/)?
                        (?:
                            (?:
                                play_redirect_hls|
                                moogaloop\.swf)\?clip_id=
                            )?
                        (?:videos?/)?
                        (?P<id>[0-9]+)
                        (?:/[\da-f]+)?
                        /?(?:[?&].*)?(?:[#].*)?$
                    '''

REGEX_YAHOO = r'(?P<url>(?P<host>https?://(?:[a-zA-Z]{2}\.)?[\da-zA-Z_-]+\.yahoo\.com)/(?:[^/]+/)*(?P<display_id>.+)?-(?P<id>[0-9]+)(?:-[a-z]+)?(?:\.html)?)'

REGEX_INS = r'(?P<url>https?://(?:www\.)?instagram\.com/p/(?P<id>[^/?#&]+))'

REGEX_BREAK = r'https?://(?:www\.)?(?P<site>break|screenjunkies)\.com/video/(?P<display_id>[^/]+?)(?:-(?P<id>\d+))?(?:[/?#&]|$)'

REGEX_FLICKER = r'https?://(?:www\.|secure\.)?flickr\.com/photos/[\w\-_@]+/(?P<id>\d+)'

REGEX_FUNNY = r'https?://(?:www\.)?funnyordie\.com/(?P<type>embed|articles|videos)/(?P<id>[0-9a-f]+)(?:$|[?#/])'

REGEX_LIVELEAK = r'https?://(?:\w+\.)?liveleak\.com/view\?(?:.*?)i=(?P<id>[\w_]+)(?:.*)'

REGEX_TED = r'''(?x)
        (?P<proto>https?://)
        (?P<type>www|embed(?:-ssl)?)(?P<urlmain>\.ted\.com/
        (
            (?P<type_playlist>playlists(?:/\d+)?) # We have a playlist
            |
            ((?P<type_talk>talks)) # We have a simple talk
            |
            (?P<type_watch>watch)/[^/]+/[^/]+
        )
        (/lang/(.*?))? # The url may contain the language
        /(?P<name>[\w-]+) # Here goes the name and then ".html"
        .*)$
        '''

REGEX_TWITCH = r'https?://(?:www\.)?twitch\.tv'

REGEX_TWITTER = r'https?://(?:www\.)?twitter\.com'

REGEX_USTREAM = r'https?://(?:www\.)?ustream\.tv/(?P<type>recorded|embed|embed/recorded)/(?P<id>\d+)'

REGEX_VIEWSTER = r'https?://(?:www\.)?viewster\.com/(?:serie|movie)/(?P<id>\d+-\d+-\d+)'
