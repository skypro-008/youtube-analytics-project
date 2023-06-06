import json
import os

from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id: str = channel_id #id канала
        channel = self._get_channel_info()
        self.title: str = channel['items'][0]['snippet']['title'] #название канала
        self.description: str = channel['items'][0]['snippet']['description'] #описание канала
        self.url: str =f'https://www.youtube.com/channel/{channel["items"][0]["id"]}' #ссылка на канал
        self.subscriber_count: int = channel['items'][0]['statistics']['subscriberCount'] #количество подписчиков
        self.video_count: int = channel['items'][0]['statistics']['videoCount'] #количество видео
        self.view_count: int = channel['items'][0]['statistics']['viewCount'] #общее количество просмотров

    def __str__(self):
        """Метод возвращает название и ссылку на канал по шаблону `<название_канала> (<ссылка_на_канал>)"""
        return f'{self.title} ({self.url})'


    def __add__(self, other):
        """Метод для суммирования общего количества подписчиков по двум каналам"""
        a = float(self.subscriber_count)
        b = float(other.subscriber_count)
        return int(a + b)

    def __sub__(self, other):
        """Метод для определения разницы в общем количестве подписчиков двух каналов"""
        a = float(self.subscriber_count)
        b = float(other.subscriber_count)
        return int(a - b)

    def __gt__(self, other):
        """Метод для операции сравнения «больше»"""
        if self.subscriber_count > other.subscriber_count:
            return True
        else:
            return False

    def __ge__(self, other):
        """Метод для операции сравнения «больше или равно»"""
        if self.subscriber_count >= other.subscriber_count:
            return True
        else:
            return False

    def __lt__(self, other):
        """Метод для операции сравнения «меньше»"""
        if self.subscriber_count < other.subscriber_count:
            return True
        else:
            return False

    def __le__(self, other):
        """Метод для операции сравнения «меньше или равно»"""
        if self.subscriber_count <= other.subscriber_count:
            return True
        else:
            return False

    def _get_channel_info(self):
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.channel = self._get_channel_info()
        return json.dump(channel, indent=2, ensure_ascii=False)


    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')  # Получен токен
        youtube = build('youtube', 'v3', developerKey=api_key)  # Специальный объект для работы с API
        return youtube

    # Геттер для channel_id
    @property
    def channel_id(self):
        return channel_id

    def to_json(self, filename):
        with open(filename, "w", encoding='utf-8') as file:
            channel_info = {
                            "channel_id": self.__channel_id,
                            "title": self.title,
                            "description": self.description,
                            "url": self.url,
                            "subscriberCount": self.subscriber_count,
                            "videoCount": self.video_count,
                            "viewCount": self.view_count
                            }
            json.dump(channel_info, file, indent=2, ensure_ascii=False)