import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Video:
    API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, video_id) -> None:
        self.video_id = video_id
        self.video_id = video_id

        try:
            self.url = f'https://youtu.be/{self.video_id}'

        except HttpError:
            self.video_info = None
            self.title = None
            self.url = None
            self.views = None
            self.like_count = None

        try:
            self.video_info = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
            self.title = self.video_info['items'][0]['snippet']['title']

        except IndexError:
            self.video_info = None
            self.title = None
            self.url = None
            self.views = None
            self.like_count = None

        else:
            self.video_id = video_id
            self.video_info = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
            self.title = self.video_info['items'][0]['snippet']['title']
            self.url = f'https://youtu.be/{self.video_id}'
            self.views = self.video_info['items'][0]['statistics']['viewCount']
            self.like_count = self.video_info['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, video_playlist):
        super().__init__(video_id)
        self.video_playlist = video_playlist

    def __str__(self):
        return f"{self.title}"
