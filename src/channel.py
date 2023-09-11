import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate

class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel_data = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_data['items'][0]['snippet']['title']
        self.description = self.channel_data['items'][0]['snippet']['description']
        self.url = self.channel_data['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscribers_count = int(self.channel_data['items'][0]['statistics']['subscriberCount'])
        self.video_count = self.channel_data['items'][0]['statistics']['videoCount']
        self.views_count = self.channel_data['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.subscribers_count + other.subscribers_count

    def __sub__(self, other):
        return self.subscribers_count - other.subscribers_count

    def __eq__(self, other):
        return self.subscribers_count == other.subscribers_count

    def __lt__(self, other):
        return self.subscribers_count < other.subscribers_count

    def __gt__(self, other):
        return self.subscribers_count > other.subscribers_count

    def __le__(self, other):
        return self.subscribers_count <= other.subscribers_count

    def __ge__(self, other):
        return self.subscribers_count >= other.subscribers_count

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_data = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel_data, indent=4, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, file_name):
        channel_info = {"id" : self.__channel_id, "title" : self.title, "description" : self.description, "url" : self.url, "subscribers_count" : self.subscribers_count, "video_count" : self.video_count, "views_count" : self.views_count}
        with open(file_name, 'w') as outfile:
            json.dump(channel_info, outfile, ensure_ascii=False)
