import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

        self.title = ''
        self.description = ''
        self.url = ''
        self.subscribers = ''
        self.video_count = ''
        self.views = ''

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube

    def get_channel(self):
        """Возвращает объект channel"""

        youtube = self.get_service()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        return channel

    def write_channel_info(self):
        """Присваивает данные"""
        channel = self.get_channel()

        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscribers = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.views = channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        channel = self.get_channel()

        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        """Сохраняет в файл значения атрибутов экземпляра `Channel`"""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscribers': self.subscribers,
            'video_count': self.video_count,
            'views': self.views
        }

        with open(file_name, 'w') as file:
            json.dump(data, file)
