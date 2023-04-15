import json
import os
import isodate
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

api_key: str = 'AIzaSyB5hhIW1yHBoo4ZoayTT0Wi4hMqhWeos9c'

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id  # id-канала
        self._description = ""  # описание канала
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"  # ссылка на канал
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self._title = channel["items"][0]['snippet']['title']
        self._subscriber_count = int(channel["items"][0]['statistics']['subscriberCount'])   # количество подписчиков
        self._video_count = int(channel["items"][0]['statistics']['videoCount'])  # количество видео
        self._view_count = int(channel["items"][0]['statistics']['viewCount'])  # количество просмотров

    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        self.print_info1()
        return self.channel_id

    @property
    def video_count(self):
        return self._video_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)

    def print_info1(self):
        apikey: str = os.getenv('YT_API_KEY')
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self._title = channel["items"][0]['snippet']['title']
        self._video_count = channel["items"][0]['statistics']['videoCount']

    def __str__(self):
        return f"'{self._title} {self.url}'"

    """
    возвращает объект для работы с YouTube API
    """
    @classmethod
    def get_service(cls):
        apikey: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=apikey)

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
        return self._subscriber_count + other._subscriber_count

    def __sub__(self, other):
        """вычитание подпищиков"""
        return self._subscriber_count - other._subscriber_count

    def __lt__(self, other):
        """метод для операции сравнения «меньше»"""
        return self._subscriber_count < other._subscriber_count

    def __le__(self, other):
        """метод для операции сравнения «меньше или равно»"""
        return self._subscriber_count <= other._subscriber_count

    def __gt__(self, other):
        """метод для операции сравнения «больше»"""
        return self._view_count > other._view_count

    def __ge__(self, other):
        """метод для операции сравнения «больше или равно»"""
        return self._view_count >= other._view_count

    def __eg__(self, other):
        """метод равенства"""
        return self._view_count == other._view_count



