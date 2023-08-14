import os
from googleapiclient.discovery import build


class APIMixin:
    """Класс для предоставления доступа к API"""

    __API_KEY: str = os.getenv('YT_API_KEY')

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API youtube"""
        service = build('youtube', 'v3', developkey=cls.__API_KEY)
        return service
