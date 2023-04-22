import os
import json
from googleapiclient.discovery import build
api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    def __init__(self, video_id: str) -> None:
        self.video_id: str = video_id
        self.video = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id).execute()
        self.title: str = self.video['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.video_id}'
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
