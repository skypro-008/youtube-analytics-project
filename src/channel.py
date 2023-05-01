import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        youtube = self.get_service()
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + channel_id
        self.subscriber_count = int(self.channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = int(self.channel["items"][0]["statistics"]["videoCount"])
        self.view_count = int(self.channel["items"][0]["statistics"]["viewCount"])

    def __str__(self):
        """Магический метод для отображения информации об объекте класса для пользователя"""

        return f'{self.title} {self.url}'

    def __add__(self, other):
        """Магический метод для складывания каналов по количеству подписчиков"""

        if isinstance(other, self.__class__):
            return self.subscriber_count + other.subscriber_count
        else:
            return self.subscriber_count + other

    def __sub__(self, other):
        """Магический метод для вычисления разницы каналов по количеству подписчиков"""

        if isinstance(other, self.__class__):
            return self.subscriberCount - other.subscriberCount
        else:
            return self.subscriberCount - other

    def __ge__(self, other):
        """Магический метод для сравнения каналов (больше или равно) по количеству подписчиков"""

        if self.subscriberCount >= other.subscriberCount:
            return True
        else:
            return False

    def __lt__(self, other):
        """Магический метод для сравнения каналов (меньше или равно) по количеству подписчиков"""

        if self.subscriberCount <= other.subscriberCount:
            return True
        else:
            return False

    def __gt__(self, other):
        """Магический метод для сравнения количества подписчиков (больше)"""
        if self.subscriberCount > other.subscriberCount:
            return True
        else:
            return False

    def __le__(self, other):
        """Магический метод для сравнения количества подписчиков (меньше)"""
        if self.subscriberCount < other.subscriberCount:
            return True
        else:
            return False

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        """Метод, сохраняющий в файл значения атрибутов экземпляра Channel"""
        dictionary = {
            'id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False)
