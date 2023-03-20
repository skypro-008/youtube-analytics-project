import json

from googleapiclient.discovery import build
import os


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.subscriber_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(self.channel['items'][0]['statistics']['viewCount'])

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, filename: str) -> None:
        with open(filename, 'w') as file:
            data = self.__dict__
            del data['channel']
            json.dump(data, file, indent=2, ensure_ascii=False)

    def __str__(self) -> str:
        """Возвращает название и ссылку на канал в формате <название_канала> (<ссылка_на_канал>)"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Складывает два канала между собой по количеству подписчиков."""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """Вычитает два канала между собой по количеству подписчиков."""
        return self.subscriber_count

    def __le__(self, other):
        """Сравнивает два канала между собой по количеству подписчиков."""
        return self.subscriber_count <= other.subscriber_count

