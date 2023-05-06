import json
import os
from googleapiclient.discovery import build

yt_api_key = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_info = {}

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.load_info()
        print(self.channel_info)

    def load_info(self):
        youtube = build('youtube', 'v3', developerKey=yt_api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.channel_info = json.dumps(channel, indent=2, ensure_ascii=False)
