import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id

        channel = Channel.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()

        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']["default"]['url']
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.views_count = channel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, new_id):
        raise AttributeError("property 'channel_id' of 'Channel' object has no setter")


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(print(json.dumps(self.youtube.channels().list(id = self.channel_id, part = 'snippet,statistics').execute(),
                               indent=2, ensure_ascii=False)))
    @classmethod

    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
    def to_json(self, moscowpython):
        list_json = {}
        list_json['id'] = self.channel_id
        list_json['title'] = self.title
        list_json['description'] = self.description
        list_json['url'] = self.url
        list_json['subscriber_count'] = self.subscriber_count
        list_json['video_count'] = self.video_count
        list_json['views_count'] = self.views_count

        with open('moscowpython.json', 'w') as f:
            json.dump(list_json, f)

