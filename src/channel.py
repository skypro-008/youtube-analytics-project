import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str, youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY_YOUTUBE'))) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = youtube

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        print(json.dumps(channel, indent=2, ensure_ascii=False))

