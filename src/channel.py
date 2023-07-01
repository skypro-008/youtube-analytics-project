import os
import json

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY: str = os.getenv('API_KEY_YOUTUBE')
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        # youtube = build('youtube', 'v3', developerKey=API_KEY)
        self.channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.__title = self.channel['items'][0]['snippet']['title']
        self.__description = self.channel['items'][0]['snippet']['description']
        self.__url = 'https://www.youtube.com/channel/' + self.channel_id
        self.__subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.__video_count = self.channel['items'][0]['statistics']['videoCount']
        self.__view_count = self.channel['items'][0]['statistics']['viewCount']

    def __repr__(self):
        return f"\"{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity})\""

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """функция сложения количества подписчиков"""
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """функция вычитания количества подписчиков"""
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        """функция сравнения количества подписчиков"""
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        """функция сравнения количества подписчиков"""
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        """функция сравнения количества подписчиков"""
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        """функция сравнения количества подписчиков"""
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        """функция сравнения количества подписчиков"""
        return int(self.subscriber_count) == int(other.subscriber_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def url(self):
        return self.__url

    @property
    def subscriber_count(self):
        return self.__subscriber_count

    @property
    def video_count(self):
        return self.__video_count

    @property
    def view_count(self):
        return self.__view_count

    @classmethod
    def get_service(cls):
        """
        возвращающий объект для работы с YouTube API
        """
        return cls.youtube

    def to_json(self, file):
        """
        Сохраняет данные в JSON файл (создает новй или перезаписывает существующий)
        атрибут file - название файла для записи.
        """
        self_dict = {'id канала': self.channel_id,
                     'название канала': self.title,
                     'описание канала': self.description,
                     'ссылка на канал': self.url,
                     'количество подписчиков': self.subscriber_count,
                     'количество видео': self.video_count,
                     'общее количество просмотров': self.view_count,
                     }
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(self_dict, f, ensure_ascii=False)