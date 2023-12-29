import os
import json
from googleapiclient.discovery import build

class Video:
    def __init__(self, video_id: str):
        self.video_id = video_id

        video_info = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id
                                       ).execute()
        
        self.video_title = video_info['items'][0]['snippet']['title']
        self.view_count = video_info['items'][0]['statistics']['viewCount']
        self.like_count = video_info['items'][0]['statistics']['likeCount']
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'

    def __str__(self) -> str:
        return self.video_title

    @classmethod
    def get_service(cls):
        """
        Класс-метод
        :return: объект для работы с YouTube API
        """
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube
    
class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id