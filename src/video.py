import json
import os
from googleapiclient.discovery import build

class Video:
    """Класс для видео"""

    def __init__(self, video_id) -> None:
        self.video_id = video_id
        self.api_key: str = os.getenv('YOUTUBE_API')
        self.video_data = None
        self.fetch_video_data()


    def fetch_video_data(self):
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        video = youtube.videos().list(id=self.video_id, part='snippet,statistics,contentDetails,topicDetails').execute()
        self.video_data = json.dumps(video, indent=2, ensure_ascii=False)

    def __str__(self):
        return self.video_title

    def my_service(self):
        return json.loads(self.video_data)

    @property
    def video_title(self) -> str:
        return self.my_service()['items'][0]['snippet']['title']

    @property
    def view_count(self):
        return self.my_service()['items'][0]['statistics']['viewCount']

    @property
    def like_count(self):
        return self.my_service()['items'][0]['statistics']['likeCount']

    @property
    def comment_count(self):
        return self.my_service()['items'][0]['statistics']['commentCount']


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
