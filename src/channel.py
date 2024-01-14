import os
import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']
        self.description = self.channel['items'][0]['snippet']['description']

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey = cls.api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        """Метод, сохраняющий в файл значения атрибутов экземпляра"""
        channel_info = {}
        channel_info["title"] = self.title
        channel_info["description"] = self.description
        channel_info["url"] = self.url
        channel_info["video_count"] = self.video_count
        channel_info["viewCount"] = self.viewCount
        channel_info["subscriber"] = self.subscriber
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(json.dumps(channel_info, indent=2, ensure_ascii=False))

    def __str__(self):
        """Магический метод __str__ для вывода названия и ссылки на канал"""
        return f"{self.title} (https://www.youtube.com/channel/{self.channel_id})"
    def __add__(self, other):
        """Магический метод сложения подписчиков"""
        return self.subscriber + other.subscriber

    def __sub__(self, other):
        """Магический метод вычитания подписчиков"""
        return self.subscriber - other.subscriber

    def __gt__(self, other):
        """Магический метод сравнения больше подписчиков"""
        return self.subscriber > other.subscriber

    def __ge__(self, other):
        """Магический метод сравнения больше или равно подписчиков"""
        return self.subscriber >= other.subscriber

    def __lt__(self, other):
        """Магический метод сравнения меньше подписчиков"""
        return self.subscriber < other.subscriber

    def __le__(self, other):
        """Магический метод сравнения меньше или равно подписчиков"""
        return self.subscriber <= other.subscriber

    def __eq__(self, other):
        """Магический метод сравнения равно подписчиков"""
        return self.subscriber == other.subscriber

###########################################