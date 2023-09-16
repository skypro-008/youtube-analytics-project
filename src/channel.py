import json
import os
from googleapiclient.discovery import build
import isodate

class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('API_KEY') # вы суки специально имя переменной в хепере для винды криво написали
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.info = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.info, indent=2, ensure_ascii=False))
