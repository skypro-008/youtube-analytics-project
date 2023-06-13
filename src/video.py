import json
import os
from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('API_KEY_YOUTUBE')

    def __init__(self, id_video):
        self.id_video = id_video
        """GET запрос по id видео с необходимыми параметрами о видео. Возвращает данные о канале в формате JSON """
        video_data = self.get_service().videos().list(id=self.id_video, part='snippet,statistics').execute()
        self.title_video = video_data['items'][0]['snippet']['title']
        self.url_video = "https://www.youtube.com/watch?v=" + self.id_video
        self.views_count_video = video_data['items'][0]['statistics']['viewCount']
        self.likes_count_video = video_data['items'][0]['statistics']['likeCount']

    @classmethod
    def get_service(cls):
        """Подключение по API к youtube. Возвращает объект для работы с YouTube API"""
        servise = build('youtube', 'v3', developerKey=Video.api_key)
        return servise

    def __str__(self):
        """Вывод информации пользоватею. Выводит наименование видео."""
        return self.title_video


class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist
