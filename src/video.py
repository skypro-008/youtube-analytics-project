import os

from googleapiclient.discovery import build

class Video:
    """ Класс для видео"""
    def __init__(self, video_id):
        """Экземпляр инициализируется реальными данными."""
        self.video_id: str = video_id #id видео
        video_response = self._get_video_info()
        self.title_video: str = video_response['items'][0]['snippet']['title'] #название видео
        self.link_to_video: str =f'https://www.youtube.com/videos/ {video_response["items"][0]["id"]}' #ссылка на видео
        self.like_count_video: int = video_response['items'][0]['statistics']['likeCount'] #количество лайков
        self.view_count_video: int = video_response['items'][0]['statistics']['viewCount'] #количество просмотров видео


    def __str__(self):
        """Метод возвращает название видео"""
        return self.title_video

    def _get_video_info(self):
        video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=self.video_id
                                       ).execute()
        return video_response

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')  # Получен токен
        youtube = build('youtube', 'v3', developerKey=api_key)  # Специальный объект для работы с API
        return youtube


class PLVideo(Video):

    def __init__(self, video_id, plvideo_id):
        """Класс для play-листов"""
        super().__init__(video_id)
        self.plvideo_id = plvideo_id
