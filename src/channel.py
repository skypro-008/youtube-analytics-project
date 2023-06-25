import os
import json
from googleapiclient.discovery import build

API_KEY: str = os.getenv('API_KEY_YOUTUBE')

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        #перенести в инит
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))



