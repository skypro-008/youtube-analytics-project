import json
import os
from typing import Any

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    channel_id = os.getenv("YT_API_KEY")
    youtube = build("youtube", "v3", developerKey=channel_id)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = (
            self.youtube.channels()
            .list(id=self.channel_id, part="snippet,statistics")
            .execute()
        )
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.id = self.channel["items"][0]["id"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.subscriber_count = self.channel["items"][0]["statistics"][
            "subscriberCount"
        ]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]

    @property
    def channel_id(self) -> str:
        """
        Вовращает id канала
        """
        return self.__channel_id

    def __str__(self):
        """
        Возвращает название канала и url
        """
        return f"{self.title}({self.url})"

    def __add__(self, other):
        """
        Возвращает сумму подписчиков двух каналов
        """
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """
        Вычетает разность подписчиков двух каналов
        """
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        """
        Возвращает False, если количество подписчиков
        текущего канала больше, чем у другого
        """
        return self.subscriber_count > other.subscriber_count

    def __le__(self, other):
        """
        Возвращает True, если количество подписчиков
        текущего канала меньше или равно, чем у другого
        """
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        """
        Возвращает True, если количество подписчиков
        у двух каналов одинаково
        """
        return self.subscriber_count == other.subscriber_count

    @classmethod
    def get_service(cls) -> Any:
        """
        Класс-метод, возвращающий объект для работы с YouTube API
        """
        channel_id = os.getenv("YT_API_KEY")
        cls.youtube = build("youtube", "v3", developerKey=channel_id)
        return cls.youtube

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel)

    def to_json(self, filename: Any) -> Any:
        """
        Функция, сохраняющая в файл значения атрибутов экземпляра Channel
        """
        channel_info = {
            "title": self.title,
            "channel_id": self.__channel_id,
            "description": self.description,
            "url": self.url,
            "count_subscriberCount": self.subscriber_count,
            "video_count": self.video_count,
            "count_views": self.view_count,
        }
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(channel_info, file, indent=4, ensure_ascii=False)
