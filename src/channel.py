import json
import os
import isodate
from googleapiclient.discovery import build

from helper.youtube_api_manual import youtube


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала и другими данными."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute())

