from src.channel import Channel
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

class Video:
    """ Инициализируется реальными данными следующих атрибутов экземпляра класса"""
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

        #youtube = Channel.get_service()
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        try:
            self.title: str = self.video_response['items'][0]['snippet']['title']
            self.url = f"https://www.youtube.com/{self.video_id}"
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']

        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None


    def __str__(self):
        return self.video_title

class PLVideo(Video):
    """Класс инициализируется  'id видео' и 'id плейлиста' """

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id



