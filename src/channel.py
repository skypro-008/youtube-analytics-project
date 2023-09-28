import json
import os
from googleapiclient.discovery import build
import isodate

api_key = 'AIzaSyDoXfDhCmEBqP323Mfo599sILGCvB9-Gb4'
#пришлось выключить, пока что не подтягивает эту переменную, хотя через консоль ее нахожу
#api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

