import os
from googleapiclient.discovery import build


class Video:
    API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, video_id) -> None:
        self.video_id = video_id
        self.video_info = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        self.title = self.video_info['items'][0]['snippet']['title']
        self.video_url = f'https://youtu.be/{self.video_id}'
        self.view_count = self.video_info['items'][0]['statistics']['viewCount']
        self.likes_count = self.video_info['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, video_playlist):
        super().__init__(video_id)
        self.video_playlist = video_playlist

    def __str__(self):
        return f"{self.title}"
