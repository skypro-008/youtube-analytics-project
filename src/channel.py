import os
import json
from googleapiclient.discovery import build

api_key: str = os.getenv("YOU_API")
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = self.print_info()['items'][0]['snippet']['title']
        self.description = self.print_info()['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber = int(self.print_info()['items'][0]['statistics']['subscriberCount'])
        self.video_count = self.print_info()['items'][0]['statistics']['videoCount']
        self.vieW = self.print_info()['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    @property
    def channel_id(self) -> str:
        return self.__channel_id

    def print_info(self) -> None:
        """Возвращает информацию о канале."""
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    @classmethod
    def get_service(cls):
        """Возвращает обьект для работы с YouTube API."""
        return build('youtube', 'v3', developerKey=os.getenv("YOU_API"))

    def to_json(self, file_name):
        """Сохраняет в файл значения атрибутов экземпляра 'Channel'."""
        data = {
            "ID": self.__channel_id,
            "Название канала": self.title,
            "Описание канала": self.description,
            "Ссылка на канал": self.url,
            "Колличество подписчиков": self.subscriber,
            "Колличество видео": self.video_count,
            "Колличество просмотров": self.vieW
        }
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def __add__(self, other):
        """
        Метод сложения
        """
        return self.subscriber + other.subscriber

    def __sub__(self, other):
        """
        Метод вычитания
        """
        return self.subscriber - other.subscriber

    def __gt__(self, other):
        """
        Метод сравнения - больше
        """
        return self.subscriber > other.subscriber

    def __ge__(self, other):
        """
        Метод сравнения - больше или равно
        """
        return self.subscriber >= other.subscriber

    def __it__(self, other):
        """
        Метод сравнения - меньше
        """
        return self.subscriber < other.subscriber

    def __le__(self, other):
        """
        Метод сравнения - меньше или равно
        """
        return self.subscriber <= other.subscriber

    def __eq__(self, other):
        """
        Метод сравнения
        """
        return self.subscriber == other.subscriber
