import json
import os

from googleapiclient.discovery import build


class YouTube:
    @classmethod
    def get_service(cls):
        api_key = os.getenv('API_Key')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


class Channel(YouTube):
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__id = channel_id
        channel = self.get_service().channels().list(id=self.__id, part='snippet,statistics').execute()
        self.ifo = channel['items'][0]
        self.items = channel['items'][0]
        self.title = self.items['snippet']['localized']['title']
        self.description = self.items['snippet']['localized']['description']
        self.url = f"https://www.youtube.com/{self.items['snippet']['customUrl']}"
        self.subscriber_count = int(self.items['statistics']['subscriberCount'])
        self.video_count = self.items['statistics']['videoCount']
        self.view_count = self.items['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        return self.ifo

    def to_json(self, filename):
        youtobe_json = {
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriberCount': self.subscriber_count,
            'videoCount': self.video_count,
            'viewCount': self.view_count,
            'id': self.__id
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(youtobe_json, f, indent=2, ensure_ascii=False)
