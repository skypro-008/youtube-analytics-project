import json
from os import environ as env
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = env.get('YT_API_KEY') if env.get('YT_API_KEY') is not None else env.get('API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id

        info = self.channel_info()['items'][0]
        self._title = info['snippet']['title']
        self._description = info['snippet']['description']
        self._url = f'https://www.youtube.com/channel/{self._channel_id}'
        self._subscriber_count = int(info['statistics']['subscriberCount'])
        self._video_count = int(info['statistics']['videoCount'])
        self._total_views = int(info['statistics']['viewCount'])

    def __str__(self):
        return f'{self.title} ({self._url})'

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

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    # getters
    @property
    def channel_id(self):
        return self._channel_id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description
    # classmethods

    @property
    def url(self):
        return self._url

    @property
    def subscriber_count(self):
        return self._subscriber_count

    @property
    def video_count(self):
        return self._video_count

    @property
    def total_views(self):
        return self._total_views

    @classmethod
    def get_service(cls):
        """
        Создает объект Resource для работы с YouTube Dara API с помощью api_key.
        :return: Объект Resource
        """
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube

    # methods
    def channel_info(self) -> dict:
        """
        Получает информацию о канале через API, путем выполнения запроса к YT Data API.
        :return: Словарь с информацией о канале
        """
        request = Channel.get_service().channels().list(part='snippet, statistics', id=self._channel_id)
        response = request.execute()

        return response

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_info())

    def to_json(self, filename: str):
        """
        Сохраняет данные канала в JSON-файл по заданному шаблону словаря.
        :param filename: Имя файла с расширением .json
        :return: None
        """
        data = {
            'channel_id': self._channel_id,
            'title': self._title,
            'description': self._description,
            'url': self._url,
            'subscriber_count': self._subscriber_count,
            'video_count': self._video_count,
            'total_views': self._total_views,
        }

        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)