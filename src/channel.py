import os
from googleapiclient.discovery import build
import json


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_id_list = []

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        channel_object = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self._channel_id = channel_id
        self.title = channel_object["items"][0]["snippet"]["title"]
        self.description = channel_object["items"][0]["snippet"]['description']
        self.url = f"https://www.youtube.com/channel/{channel_object['items'][0]['id']}"
        self.subscriber_count = channel_object["items"][0]['statistics']['subscriberCount']
        self.video_count = channel_object["items"][0]['statistics']['videoCount']
        self.view_count = channel_object["items"][0]['statistics']['viewCount']
        self.channel_id_list.append(self)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.channel_id

    @channel_id.setter
    def channel_id(self):
        raise AttributeError

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, path):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(self.__dict__, file, ensure_ascii=False)
