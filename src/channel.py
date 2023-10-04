import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """
    Класс для ютуб-канала
    """
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.__channel_id = None
        self.channel_id = channel_id
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """
        Класс метод возвращающий объект для работы с YouTube API
        """
        return Channel.youtube

    def to_json(self, name: str):
        """
        Метод сохраняющий в файл значения атрибутов экземпляра `Channel`
        """
        temp_dict = {
            '__channel_id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(name, "w", encoding='utf-8') as file:
            json.dump(temp_dict, file, ensure_ascii=False)

    def __str__(self):
        """
        Метод возвращает информацию об объекте для пользователя
        return: '<название канала> <url адрес канала>'
        """
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """
        Метод позволяет складывать количество подписчиков у объектов,
        если они принадлежат одному классу
        return: Сумму количества подписчиков
        """
        if isinstance(self, Channel) and isinstance(other, Channel):
            return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """"
        Метод позволяет вычитать количество подписчиков у объектов,
        если они принадлежат одному классу
        return: Разность количества подписчиков
        """
        if isinstance(self, Channel) and isinstance(other, Channel):
            return int(self.subscriber_count) - int(other.subscriber_count)

    def __eq__(self, other):
        """"
        Метод позволяет проверять на равенство количество подписчиков у объектов,
        если они принадлежат одному классу
        return: True или False
        """
        if isinstance(self, Channel) and isinstance(other, Channel):
            return int(self.subscriber_count) == int(other.subscriber_count)

    def __gt__(self, other):
        """"
        Метод позволяет проверять больше ли количество
        подписчиков у первого объекта, чем у второго,
        если они принадлежат одному классу
        return: True или False
        """
        if isinstance(self, Channel) and isinstance(other, Channel):
            return int(self.subscriber_count) > int(other.subscriber_count)

    def __lt__(self, other):
        """"
        Метод позволяет проверять меньше ли количество
        подписчиков у первого объекта, чем у второго,
        если они принадлежат одному классу
        return: True или False
        """
        if isinstance(self, Channel) and isinstance(other, Channel):
            return int(self.subscriber_count) < int(other.subscriber_count)

    def __ge__(self, other):
        """"
        Метод позволяет проверять больше либо равно количество
        подписчиков у первого объекта, чем у второго,
        если они принадлежат одному классу
        return: True или False
        """
        if isinstance(self, Channel) and isinstance(other, Channel):
            return int(self.subscriber_count) >= int(other.subscriber_count)

    def __le__(self, other):
        """"
        Метод позволяет проверять меньше либо равно количество
        подписчиков у первого объекта, чем у второго,
        если они принадлежат одному классу
        return: True или False
        """
        if isinstance(self, Channel) and isinstance(other, Channel):
            return int(self.subscriber_count) <= int(other.subscriber_count)