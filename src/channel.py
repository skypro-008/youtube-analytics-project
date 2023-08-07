import json
import os

from googleapiclient.discovery import build

import helper.youtube_api_manual


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.subscriberCount = self.channel["items"][0]["statistics"]["subscriberCount"]

    def __str__(self):
        return f'{self.title} ({self.url})'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.channel = json.dumps(self.channel, indent=2, ensure_ascii=False)
        print(f'{self.channel}')

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("False name or invalid")

    @classmethod
    def get_service(self):
        self.API_KEY = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey='AIzaSyAZomY9PsOL0gNN8BbgrlbNo9z6BVbmR7s')
        return helper.youtube

    @classmethod
    def to_class(cls, obj):
        if not isinstance(obj, Channel):
            raise TypeError('Операнд справа должен быть экземпляром класса '
                            'Channel!')
        return obj.subscriberCount

    def to_json(self, file_name=None):
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriberCount': self.subscriberCount,
            'video_count': self.video_count,
            'viewCount': self.viewCount
        }
        with open(file_name, 'w') as file:
            json.dump(self.channel, file)

    def get_channel(self):
        return self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def __add__(self, other):
        if isinstance(other, Channel):
            return self.subscriberCount + other.subscriberCount
        else:
            raise TypeError('Операнд справа должен быть экземпляром класса Channel!')

    def __sub__(self, other):
        if isinstance(other, Channel):
            return self.subscriberCount - other.subscriberCount
        else:
            raise TypeError('Операнд справа должен быть экземпляром класса Channel!')

    def __gt__(self, other):
        if isinstance(other, Channel):
            return self.subscriberCount > other.subscriberCount
        else:
            raise TypeError('Операнд справа должен быть экземпляром класса Channel!')

    def __ge__(self, other):
        if isinstance(other, Channel):
            return self.subscriberCount >= other.subscriberCount
        else:
            raise TypeError('Операнд справа должен быть экземпляром класса Channel!')

    def __lt__(self, other):
        if isinstance(other, Channel):
            return self.subscriberCount < other.subscriberCount
        else:
            raise TypeError('Операнд справа должен быть экземпляром класса Channel!')

    def __le__(self, other):
        if isinstance(other, Channel):
            return self.subscriberCount <= other.subscriberCount
        else:
            raise TypeError('Операнд справа должен быть экземпляром класса Channel!')

    def __eq__(self, other):
        if isinstance(other, Channel):
            return self.subscriberCount == other.subscriberCount
        else:
            raise TypeError('Операнд справа должен быть экземпляром класса Channel!')

    def __sub__(self, other):
        if isinstance(other, Channel):
            return int(self.subscriberCount) - int(other.subscriberCount)
        else:
            raise TypeError('Операнд справа должен быть экземпляром класса Channel!')






