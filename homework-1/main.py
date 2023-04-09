from src.channel import Channel

import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

if __name__ == '__main__':
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    channel = youtube.channels().list(id=vdud, part='snippet,statistics').execute()
    vdud.print_info(channel)
    playlists = youtube.playlists().list(channelId=vdud,
                                         part='contentDetails,snippet',
                                         maxResults=50,
                                         ).execute()
    # printj(playlists)
    for playlist in playlists['items']:
        print(playlist)
        print()

    '''
    получить данные по видеороликам в плейлисте
    docs: https://developers.google.com/youtube/v3/docs/playlistItems/list

    получить id плейлиста можно из браузера, например
    https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb
    или из ответа API: см. playlists выше
    '''
    # playlist_id = 'PLguYHBi01DWrlpOkXwOYe8qjGFyqobcoO'
    playlist_id = 'PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'
    playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                   part='contentDetails',
                                                   maxResults=50,
                                                   ).execute()
    # printj(playlist_videos)

    # получить все id видеороликов из плейлиста
    video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
    # print(video_ids)

    '''
    вывести длительности видеороликов из плейлиста
    docs: https://developers.google.com/youtube/v3/docs/videos/list
    '''

    '''
    получить статистику видео по его id
    получить id можно из адреса видео
    https://www.youtube.com/watch?v=9lO06Zxhu88 или https://youtu.be/9lO06Zxhu88
    '''
    video_id = '9lO06Zxhu88'
    video_id = '9lO06Zxhu88'  # дудь кремниевая долина
    video_id = '4jRSy-_CLFg'  # Редакция плейлист анти-тревел
    video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                           id=video_id
                                           ).execute()
    # printj(video_response)
    video_title: str = video_response['items'][0]['snippet']['title']
    view_count: int = video_response['items'][0]['statistics']['viewCount']
    like_count: int = video_response['items'][0]['statistics']['likeCount']
    comment_count: int = video_response['items'][0]['statistics']['commentCount']

    """
{
  "kind": "youtube#channelListResponse",
  "etag": "TUX2o600Qs42JSCO9hckmDv7scY",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "SsK2QuB-f3WnRrph7tt5yppfuN8",
      "id": "UCMCgOm8GZkHp8zJ6l7_hIuA",
      "snippet": {
        "title": "вДудь",
        "description": "Здесь задают вопросы",
        "customUrl": "@vdud",
        "publishedAt": "2014-01-03T06:27:22Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "вДудь",
          "description": "Здесь задают вопросы"
        }
      },
      "statistics": {
        "viewCount": "1925259492",
        "subscriberCount": "10300000",
        "hiddenSubscriberCount": false,
        "videoCount": "163"
      }
    }
  ]
}
    """