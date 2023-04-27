import json
from googleapiclient.discovery import build
import os


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('API_KEY_YOU_TUBE')
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'
    dict_to_print = []

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

    def __str__(self):
        """Метод для отображения информации об объекте класса для пользователей"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """ Метод добавления"""
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other):
        """Метод вычетание"""
        return int(self.subscriberCount) - int(other.subscriberCount)

    def __gt__(self, other):
        """ Метод сравнения (больше)"""
        return int(self.subscriberCount) > int(other.subscriberCount)

    def __ge__(self, other):
        """ Метод сравнения (больше или равно)"""
        return int(self.subscriberCount) >= int(other.subscriberCount)

    def __lt__(self, other):
        """ Метод сравнения (меньше)"""
        return int(self.subscriberCount) < int(other.subscriberCount)

    def __le__(self, other):
        """ Метод сравнения (меньше или равно)"""
        return int(self.subscriberCount) <= int(other.subscriberCount)

    def __eq__(self, other):
        """ Метод сравнения (равно)"""
        return int(self.subscriberCount) == int(other.subscriberCount)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(f'Информацию о канале{self.channel}')

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, dict_to_print) -> None:
        """Сохраняет в файл значения атрибутов экземпляра `Channel`"""

        with open(dict_to_print, "w", encoding='utf-8') as write_file:
            json.dump({"title": self.title,
                       "description": self.description,
                       "url": self.url,
                       "subscriberCount": self.subscriberCount,
                       "video_count": self.video_count,
                       "viewCount": self.viewCount}, write_file, indent=2, ensure_ascii=False, separators=(',', ': '))
            print(dict_to_print)
