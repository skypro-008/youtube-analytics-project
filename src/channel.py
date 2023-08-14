import os
import json
from src.apimixin import APIMixin
from googleapiclient.discovery import build


class Channel(APIMixin):
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = Channel.get_service().channels().list(
            id=channel_id, part='snippet,statistics'
        ).execute()

        self.id = self.channel['items'][0]['id']
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.custom_url = self.channel['items'][0]['snippet']['customUrl']
        self.url = f'https://www.youtube.com/{self.custom_url}'
        self.subscribes_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']


    @property
    def channel_id(self):
        return self.__channel_id


    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)


    def __str__(self):
        return f'{self.title} (https://www.youtube.com/channel/{self.__channel_id})'


    def __add__(self, other):
        plus = int(self.view_count) + int(other.view_count)
        return plus


    def __sub__(self, other):
        minus = int(self.view_count) - int(other.view_count)
        return minus


    def __gt__(self, other):
        more = int(self.view_count) > int(other.view_count)
        return more


    def __ge__(self, other):
        more_equals = int(self.view_count) >= int(other.view_count)
        return more_equals


    def __lt__(self, other):
        less = int(self.view_count) < int(other.view_count)
        return less


    def __le__(self, other):
        less_equals = int(self.view_count) <= int(other.view_count)
        return less_equals


    def __eq__(self, other):
        equals = int(self.view_count) == int(other.view_count)
        return equals


    def to_json(self, path):
        data = self.__dict__
        del data["channel"]
        with open(path, 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
