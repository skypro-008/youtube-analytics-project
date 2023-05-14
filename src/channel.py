import json
import os

from googleapiclient.discovery import build

api_key: str = os.getenv('API_KEY_YT')
youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()["items"][0]

        self.title = channel["snippet"]["title"]
        self.description = channel["snippet"]["description"]
        self.url = channel["snippet"]["customUrl"]
        self.subscriber_count = int(channel["statistics"]["subscriberCount"])
        self.video_count = channel["statistics"]["videoCount"]
        self.view_count = channel["statistics"]["viewCount"]

    def __str__(self):
        return f"{self.title} {self.url}"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count







    def print_info(self) -> str:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel))

    @classmethod
    def get_service(cls):
        return youtube

    def to_json(self, path):
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count

        }
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file)
