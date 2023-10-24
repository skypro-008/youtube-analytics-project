import os
import json
from googleapiclient.discovery import build


class Channel:
    api_key = os.getenv('YouTubeAPI')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        self._channel_id = channel_id
        self.update_info()

    def update_info(self):
        channel = self.youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        if 'items' in channel and len(channel['items']) > 0:
            self.title = channel['items'][0]['snippet']['title']
            self.description = channel['items'][0]['snippet']['description']
            self.url = 'https://www.youtube.com/channel/' + self._channel_id
            self.subscriberCount = channel['items'][0]['statistics']['subscriberCount']
            self.videoCount = channel['items'][0]['statistics']['videoCount']
            self.viewCount = channel['items'][0]['statistics']['viewCount']
        else:
            print(f'No channel information returned for id {self._channel_id}')
            self.title = None
            self.description = None
            self.url = None
            self.subscriberCount = None
            self.videoCount = None
            self.viewCount = None

    def print_info(self):
        print(f'Channel ID: {self._channel_id}')
        print(f'Title: {self.title}')
        print(f'Description: {self.description}')
        print(f'URL: {self.url}')
        print(f'Subscriber Count: {self.subscriberCount}')
        print(f'Video Count: {self.videoCount}')
        print(f'View Count: {self.viewCount}')

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
        self.update_info()

    def to_json(self, file_name='channel_info.json'):
        info = {
            'Channel ID': self._channel_id,
            'Title': self.title,
            'Description': self.description,
            'URL': self.url,
            'Subscriber Count': self.subscriberCount,
            'Video Count': self.videoCount,
            'View Count': self.viewCount
        }
        with open(file_name, 'w') as f:
            json.dump(info, f, indent=4)


    def __add__(self, other):
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other):
        return self.subscriberCount - other.subscriberCount

    def __sub__(self, other):
        return int(other.subscriberCount) - int(self.subscriberCount)


    def __gt__(self, other):
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other):
        return self.subscriberCount >= other.subscriberCount

    def __lt__(self, other):
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other):
        return self.subscriberCount <= other.subscriberCount

    def __eq__(self, other):
        return self.subscriberCount == other.subscriberCount