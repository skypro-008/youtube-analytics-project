
import json
import os
from googleapiclient.discovery import build

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.api_key: str = os.getenv('YT_API_KEY')
        self.channel_id = channel_id

    def __repr__(self):
        """Возвращает строковое представление класса"""
        return f'class Channel(API_KEY:"{self.api_key}", CHANNEL_ID:"{self.channel_id}")'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        youtube = build('youtube', 'v3', developerKey=self.api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        printj(channel)