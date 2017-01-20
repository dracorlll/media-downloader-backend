regex_yt = r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$'
regex_vk = r'''(?x)
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
regex_fb = r'''(?x)
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
regex_dm = r'(?i)(?:https?://)?(?:(www|touch)\.)?dailymotion\.[a-z]{2,3}/(?:(?:embed|swf|#)/)?video/(?P<id>[^/?_]+)'
regex_ru = r'https?://(?:(?:www|m)\.)?my\.mail\.ru/(?:video/.*#video=/?(?P<idv1>(?:[^/]+/){3}\d+)|(?:(?P<idv2prefix>(?:[^/]+/){2})video/(?P<idv2suffix>[^/]+/\d+))\.html)'
regex_url = r'[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
regex_vimeo = r'''(?x)
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
regex_yahoo = r'(?P<url>(?P<host>https?://(?:[a-zA-Z]{2}\.)?[\da-zA-Z_-]+\.yahoo\.com)/(?:[^/]+/)*(?P<display_id>.+)?-(?P<id>[0-9]+)(?:-[a-z]+)?(?:\.html)?)'
