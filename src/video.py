import os
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
from urllib.request import urlopen
from urllib.error import HTTPError
class Video:
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    title = None
    url = None
    views_count = None
    like_count = None

    def __init__(self, video_id):
        self.video_id = video_id

        try:
            self.video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                              id=self.video_id).execute()

            self.title = self.video_response['items'][0]['snippet']['title']
            self.url = self.video_response['items'][0]['snippet']['thumbnails']['default']['url']
            self.views_count = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count = self.video_response['items'][0]['statistics']['likeCount']
        except (IndexError, HTTPError, IndexError):
            print('Video_id некорректен')

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
