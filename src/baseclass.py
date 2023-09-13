import os
from googleapiclient.discovery import build


class MixinBase:
    """Абстрактный класс, который вернет объект для работы с YouTube API"""

    # API_KEY_YOUTUBE скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('API_KEY')

    @classmethod
    def get_service(cls):
        """возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=cls.api_key)