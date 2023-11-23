import os

from googleapiclient.discovery import build


class YouTube:
    @classmethod
    def get_service(cls):
        api_key = os.getenv('API_Key')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


class Channel(YouTube):
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__id = channel_id
        channel = self.get_service().channels().list(id=self.__id, part='snippet,statistics').execute()
        self.ifo = channel

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        return self.ifo
