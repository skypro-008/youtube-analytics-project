import json
import os
from googleapiclient.discovery import build
import isodate

api_key = 'AIzaSyDoXfDhCmEBqP323Mfo599sILGCvB9-Gb4'

youtube = build('youtube', 'v3', developerKey=api_key)
channel = youtube.channels().list(id='UC-OVMPlMA3-YCIeg4z5z23A', part='snippet,statistics').execute()

print(youtube)






{'kind': 'youtube#channelListResponse',
 'etag': 'WO_oOipUFQCGzvojWpd8sg9osUA',
 'pageInfo':
     {'totalResults': 1, 'resultsPerPage': 5},
 'items':
     [{'kind': 'youtube#channel',
       'etag': 'egfL1jK3GdLX2FlZfRwyPMd9Fok',
       'id': 'UC-OVMPlMA3-YCIeg4z5z23A',
       'snippet':
           {'title': 'MoscowPython',
            'description': 'Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)',
            'customUrl': '@moscowdjangoru',
            'publishedAt': '2012-07-13T09:48:44Z',
            'thumbnails':
                {'default':
                     {'url': 'https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s88-c-k-c0x00ffffff-no-rj',
                      'width': 88,
                      'height': 88},
                 'medium':
                     {'url': 'https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s240-c-k-c0x00ffffff-no-rj',
                      'width': 240,
                      'height': 240},
                 'high':
                     {'url': 'https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s800-c-k-c0x00ffffff-no-rj',
                      'width': 800,
                      'height': 800}},
            'localized':
                {'title': 'MoscowPython',
                 'description': 'Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)'},
            'country': 'RU'},
       'statistics':
           {'viewCount': '2423559',
            'subscriberCount': '26500',
            'hiddenSubscriberCount': False,
            'videoCount': '708'}}]}


