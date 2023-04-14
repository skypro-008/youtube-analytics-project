import json
import os
import requests
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv("YT_API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        if self.channel_id is None:
            self.channel_id = channel_id

      #  self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        # self.url = self.channel2  # ['items'][0]['snippet']['customUrl']
        self.subscriberCount = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']

    # @property
    # def channel_id_(self):
    #     return self.channel_id
    #
    # @channel_id_.setter
    # def change_id(self, channel_id):
    #     if self.channel_id is None:
    #         self.channel_id = channel_id
    #     else:
    #         print("AttributeError: property 'channel_id' of 'Channel' object has no setter")

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.youtube

    def __repr__(self):
        return f'{self.channel_id}'
