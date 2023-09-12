import os
from googleapiclient.discovery import build

class Video:
    api_key = os.getenv('YT_API_KEY')
    def __init__(self, id):
        self.video_id = id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.video_data = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        self.title = self.video_data['items'][0]['snippet']['title']
        self.url = self.video_data['items'][0]['snippet']['thumbnails']['default']['url']
        self.views_count = self.video_data['items'][0]['statistics']['viewCount']
        self.likes_count = self.video_data['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f"{self.title}"

class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
