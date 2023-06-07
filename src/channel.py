import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel = None
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + self.__channel_id
        self.subscriberCount = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.viewCount = self.channel["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel = json.dumps(self.channel, indent=2, ensure_ascii=False)

        print(self.channel)

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.API_KEY)

    def to_json(self, file_name):
        with open(file_name, "w") as file:
            json.dump(json.dumps(self.__channel_id), file)
            json.dump(self.title, file)
            json.dump(self.description, file)
            json.dump(self.url, file)
            json.dump(self.subscriberCount, file)
            json.dump(self.video_count, file)
            json.dump(self.viewCount, file)

    @property
    def channel_id(self):
        return

    @channel_id.setter
    def channel_id(self, value):
        print("AttributeError: property 'channel_id' of 'Channel' object has no setter")
