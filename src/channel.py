import pickle
import json

from googleapiclient.discovery import build

import os


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('API_KEY_YOU_TUBE')
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'
    dict_to_print = []

    #

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriberCount = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(f'Информацию о канале{self.channel}')

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, dict_to_print: dict) -> None:
        self.dict_to_print.append([self.title, self.description, self.url, self.subscriberCount,
                                                  self.video_count, self.viewCount])

        """Сохраняет в файл значения атрибутов экземпляра `Channel`"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
