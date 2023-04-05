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
        """вывод информации о канале"""
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()


        print(json.dumps(channel, indent=2, ensure_ascii=False))
