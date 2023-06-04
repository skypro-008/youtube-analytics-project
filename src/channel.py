import json
import os
from googleapiclient.discovery import build
import isodate


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('API_KEY_YOUTUBE')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def get_service(self):
        servise = build('youtube', 'v3', developerKey=Channel.api_key)
        return servise

    def get_channel_info(self):
        r = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return json.dumps(r)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.get_channel_info())
