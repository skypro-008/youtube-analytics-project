from googleapiclient.discovery import build
import os


class Video:
    """Класс для видео"""

    api_key = os.getenv('YT_API_KEY')

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется по id видео. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        self.video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                               id=video_id).execute()
        try:
            self.title: str = self.video_response['items'][0]['snippet']['title']
            self.url = f"https://www.youtube.com/video/{self.video_id}"
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
            self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']
        except IndexError:
            self.title = None
            self.like_count = None
            self.view_count = None
            self.url = None
            self.comment_count = None
    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=cls.api_key)

    def __str__(self):
        """Магический метод __str__ для вывода названия и ссылки на канал"""
        return f"{self.video_title}"


class PLVideo(Video):
    """Класс для плейлиста"""

    def __init__(self, video_id: str, playlist_id: str):
        """Экземпляр инициализируется по id видео и id плейлиста. Дальше все данные будут подтягиваться по API."""
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.playlist_response = self.get_service().playlistItems().list(playlistId=playlist_id,
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute()
