import json
import os

from googleapiclient.discovery import build

api_key: str = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel = youtube.channels().list(id=self.id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
