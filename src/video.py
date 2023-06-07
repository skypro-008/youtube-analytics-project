import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
class Video:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.title = None
        self.url = None
        self.view_count = None
        self.like_count = None

        video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()

        # Обработка результата
        self.title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.url = 'https://youtu.be/' + self.video_id

    def __str__(self):
        return self.title

class PLVideo(Video):
    def __init__(self, video_id, pl_id):
        super().__init__(video_id)
        self.pl_id = pl_id





