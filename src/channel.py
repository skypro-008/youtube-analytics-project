import json
import os
import re

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self.api_key = os.getenv('YOUTUBE_API')
        self.channel_data = None
        self.fetch_channel_data()

    def __str__(self):
        pattern = r'https?://[^\s!"?]+'
        description = self.description
        matches = re.findall(pattern, description)
        return f"{self.title} ({''.join(matches)})"

    def fetch_channel_data(self):
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.channel_data = json.dumps(channel, indent=2, ensure_ascii=False)

    def channel_json(self):
        return self.channel_data

    def my_service(self):
        """Создаем json файл без лишних данных"""
        return json.loads(self.channel_data)['items'][0]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_data)

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, new_channel_id):
        raise AttributeError("Attribute 'channel_id' of 'Channel' object has no setter.")

    @property
    def title(self):
        return self.my_service()['snippet']['title']

    @property
    def description(self):
        return self.my_service()['snippet']['description']

    @property
    def video_count(self):
        return self.my_service()['statistics']['videoCount']

    @property
    def url(self):
        return self.my_service()['snippet']['thumbnails']['default']['url']

    @property
    def subscriber_count(self):
        return self.my_service()['statistics']['subscriberCount']

    @property
    def view_count(self):
        return self.my_service()['statistics']['viewCount']

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        api_key = os.getenv('YOUTUBE_API')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        """ Cоздаем файл 'moscowpython.json' c данными по каналу """
        with open(filename, 'w') as f:
            json.dump(self.my_service(), f, indent=2, ensure_ascii=False)

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)
