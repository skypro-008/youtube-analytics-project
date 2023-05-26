import json
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()


class Channel:
    yt_api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=yt_api_key)

    def __init__(self, channel_id: str) -> None:
        self.__channel_id = channel_id
        self.title = None
        self.description = None
        self.url = None
        self.subscriber_count = None
        self.video_count = None
        self.view_count = None

        self.__update_attributes()

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def print_info(self) -> None:
        print(self.__get_build())

    def __get_build(self) -> dict:
        channel_dict = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel_dict

    def __update_attributes(self) -> None:
        data = self.__get_build()

        self.title = data.get('items')[0].get('snippet').get('title')
        self.description = data.get('items')[0].get('snippet').get('description')
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscriber_count = data.get('items')[0].get('statistics').get('subscriberCount')
        self.video_count = data.get('items')[0].get('statistics').get('videoCount')
        self.view_count = data.get('items')[0].get('statistics').get('viewCount')

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, file_name: str) -> None:
        data = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count,
        }

        with open(file_name, 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
