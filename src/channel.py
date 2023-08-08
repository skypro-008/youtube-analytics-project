import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        snippet = channel['items'][0]['snippet']
        statistics = channel['items'][0]['statistics']

        self.__name = snippet['title']
        self.__description = snippet['description']
        self.__url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.__subscriber_count = int(statistics['subscriberCount'])
        self.__video_count = int(statistics['videoCount'])
        self.__view_count = int(statistics['viewCount'])

    def __str__(self):
        """
        Метод возвращающий название и ссылку на канал
        """
        return f"{self.__name} ({self.__url})"

    def __add__(self, other):
        """
        Метод сложения по количеству подписчиков
        """
        return self.__subscriber_count + other.__subscriber_count

    def __sub__(self, other):
        """
        Метод вычитания по количеству подписчиков
        """
        return self.__subscriber_count - other.__subscriber_count

    def __lt__(self, other):
        """
        Метод сравнения по количеству подписчиков
        """
        return self.__subscriber_count < other.__subscriber_count

    def __le__(self, other):
        return self.__subscriber_count <= other.__subscriber_count

    def __gt__(self, other):
        return self.__subscriber_count > other.__subscriber_count

    def __ge__(self, other):
        return self.__subscriber_count >= other.__subscriber_count

    @property
    def channel_id(self) -> str:
        return self.__channel_id

    @property
    def title(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def url(self) -> str:
        return self.__url

    @property
    def subscriber_count(self) -> int:
        return self.__subscriber_count

    @property
    def video_count(self) -> int:
        return self.__video_count

    @property
    def view_count(self) -> int:
        return self.__view_count

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        return cls.youtube

    def to_json(self, file_path: str) -> None:
        """Сохраняет значения атрибутов экземпляра Channel в файл в формате JSON."""
        data = {
            'channel_id': self.__channel_id,
            'name': self.__name,
            'description': self.__description,
            'url': self.__url,
            'subscriber_count': self.__subscriber_count,
            'video_count': self.__video_count,
            'view_count': self.__view_count
        }
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
