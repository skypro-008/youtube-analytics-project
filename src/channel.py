import json
import os
import isodate
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self._title = channel["items"][0]['snippet']['title']
        self._description = ""
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self._subscriber_count = ""
        self._video_count = int(channel["items"][0]['statistics']['videoCount'])   # количество видео
        self._view_count = int(channel["items"][0]['statistics']['viewCount'])    #количество просмотров


    @property
    def channel_id(self):
        """Название канала, в виде переменной"""

        return self.__channel_id

    @property
    def title(self):
        """Название канала в виде переменной"""

        return self._title

    @property
    def video_count(self):
        """Количество видео на канале"""

        return self._video_count

    def __str__(self):
        return f"'{self._title} {self.url}'"

    def print_info(self):
        """Вывод информации о канале"""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        printj = json.dumps(channel, indent=2, ensure_ascii=False)
        return print(printj)

    @classmethod
    def get_service(cls):
        """Класс метод возвращающий объект для работы с YouTube API"""
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        """Создание файла json из атрибутов класса"""
        data = {
            "channel_id": self.__channel_id,
            "title": self.title,
            "description": self._description,
            "url": self.url,
            "subscriber_count": self._subscriber_count,
            "video_count": self._video_count,
            "view_count": self._view_count
        }
        with open(filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


    def __add__(self, other):
        """сложение подпищиков"""
        return self._view_count + other._view_count

    def __sub__(self, other):
        """вычитание подпищиков"""
        return self._view_count - other._view_count

    def __lt__(self, other):
        """метод для операции сравнения «меньше»"""
        return self._view_count < other._view_count

    def __le__(self, other):
        """метод для операции сравнения «меньше или равно»"""
        return self._view_count <= other._view_count

    def __gt__(self, other):
        """метод для операции сравнения «больше»"""
        return self._view_count > other._view_count

    def __ge__(self, other):
        """метод для операции сравнения «больше или равно»"""
        return self._view_count >= other._view_count

    def __eg__(self, other):
        """метод равенства"""
        return self._view_count == other._view_count

