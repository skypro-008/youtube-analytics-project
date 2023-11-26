import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.id = self.channel["items"][0]["id"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.subscriberCount = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.viewCount = self.channel["items"][0]["statistics"]["viewCount"]

    def print_info(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        print(json.dumps(self.channel))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, filename):
        channel_info = {"title": self.title,
                        "channel_id": self.__channel_id,
                        "description": self.description,
                        "url": self.url,
                        "count_subscriberCount": self.subscriberCount,
                        "video_count": self.video_count,
                        "count_views": self.viewCount}
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(channel_info, file, indent=4, ensure_ascii=False)
