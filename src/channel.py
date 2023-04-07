import json
import os
import isodate
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self):
        """Вывод информации о канале"""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        info_canal = json.dumps(channel, indent=2, ensure_ascii=False)

        return print(info_canal)


    def get_service(self):
        """Возвращает объект для работы с YouTube API"""
        pass


    def to_json(self):
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        pass