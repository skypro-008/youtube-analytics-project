import pandas as pd
import json
import os

from googleapiclient.discovery import build

from helper.youtube_api_manual import youtube


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала и другими данными."""
        self.__channel_id = channel_id
        self.chanel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.description = self.chanel['items'][0]['snippet']['description']
        self.count_subscribers = self.chanel['items'][0]['statistics']['subscriberCount']
        self.view_count = self.chanel['items'][0]['statistics']['viewCount']
        self.title = self.chanel['items'][0]['snippet']['title']
        self.video_count = self.chanel['items'][0]['statistics']['videoCount']
        self.url = f'https://www.youtube.com/channel/{self.chanel['items'][0]['id']}'

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        self.__channel_id = channel_id

    def print_info(self) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        # print(self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute())
        print(self.chanel)

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, param):
        channel_info = {"title": self.title,
                        "channel_id": self.channel_id,
                        "description": self.description,
                        "url": self.url,
                        "count_subscribers": self.count_subscribers,
                        "video_count": self.video_count,
                        "viewCount": self.view_count}
        with open(param, 'w', encoding='utf-8') as file:
            json.dump(channel_info, file, indent=4, ensure_ascii=False)
