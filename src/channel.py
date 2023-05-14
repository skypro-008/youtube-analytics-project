import json
import os
from googleapiclient.discovery import build

API_KEY: str = os.getenv('YT_API_KEY')
YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel = YOUTUBE.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = channel_id
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    # @property
    # def channel_id(self):
    #     return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @staticmethod
    def get_service():
        return YOUTUBE

    def to_json(self, path):
        channel_info = {
            "id": self.__channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.subscriber_count,
            "videoCount": self.video_count,
            "viewCount": self.view_count
        }
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(channel_info, file, indent=1, ensure_ascii=False)
