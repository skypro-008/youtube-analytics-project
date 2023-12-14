import json
import os
from googleapiclient.discovery import build

import isodate


class Channel:
    """Класс для ютуб-канала"""

    YT_API_KEY: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.pk = self.channel["items"][0]["id"]
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A{self.__channel_id}'
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]

    def __str__(self):
        return f"'{self.title} ({self.url})'"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

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

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel))

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=cls.YT_API_KEY)
        return youtube

    def to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.channel))
