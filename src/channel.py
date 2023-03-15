import json
import os
from googleapiclient.discovery import build


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:
    """Класс для ютуб-канала"""

    @staticmethod
    def get_service():
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.api_key: str = os.getenv('YT_API_KEY')
        self.__channel_id = channel_id
        youtube = Channel.get_service()
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        self.subscriber_count = int(self.channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = int(self.channel["items"][0]["statistics"]["videoCount"])
        self.view_count = int(self.channel["items"][0]["statistics"]["viewCount"])

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __repr__(self):
        """Возвращает строковое представление класса"""
        return f'class Channel(API_KEY:"{self.api_key}", CHANNEL_ID:"{self.__channel_id}")'

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        printj(self.channel)

    def to_json(self, fname):
        out = {"id": self.__channel_id, "title": self.title, "description": self.description,
               "url": self.url, "subscriberCount": self.subscriber_count,
               "videoCount": self.video_count, "viewCount": self.view_count}
        with open(fname, 'w', encoding="utf-8") as file:
            json.dump(out, file, indent=2, ensure_ascii=False)

    def __add__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count + other.subscriber_count
        else:
            raise TypeError("ERROR: class Channel + other type not implemented")

    def __sub__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count - other.subscriber_count
        else:
            raise TypeError("ERROR: class Channel - other type not implemented")
        
    def __ge__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count >= other.subscriber_count
        else:
            raise TypeError("ERROR: class Channel >= other type not implemented")

