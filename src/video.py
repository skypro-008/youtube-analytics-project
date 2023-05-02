import os
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
from urllib.request import urlopen
from urllib.error import HTTPError
class Video:
    def __init__(self, video_id: str) -> None:
        self.video_id: str = video_id
        self.url = f'https://youtu.be/{self.video_id}'
        try:
            urlopen(self.url)
        except HTTPError as err:
            if err.code == 404:
                print('Несуществующий url')
        self.video = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id).execute()
        try:
            self.title: str = self.video['items'][0]['snippet']['title']
        except (ValueError,IndexError):
            print(' Ошибка')
            self.view_count = None
            self.like_count = None
            self.comment_count = None
            self.video_count = None
            self.title: str = None
        else:
            self.view_count: int = self.video['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video['items'][0]['statistics']['likeCount']
            self.comment_count: int = self.video['items'][0]['statistics']['commentCount']
            self.video_count: int = self.video['items'][0]['statistics']['viewCount']
    def __str__(self):
        return f'{self.title}'

class PLVideo:
    def __init__(self, video_id, playlist_id) -> None:
        self.video_id = video_id
        self.video = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                           id=video_id).execute()
        self.title = self.video['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.video_id}'
        self.view_count: int = self.video['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video['items'][0]['statistics']['likeCount']
        self.playlist_id = playlist_id
    def __str__(self):
        return f'{self.title}'
