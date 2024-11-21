from dotenv import load_dotenv
import os
import json
from googleapiclient.discovery import build

load_dotenv()


class Channel:
    """Класс для ютуб-канала"""
    API_KEY = os.getenv("YOUTUBE_API")

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.channel_info = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.count_subscribers = self.channel['items'][-1]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][-1]['statistics']['videoCount']
        self.all_views = self.channel['items'][-1]['statistics']['viewCount']

    @staticmethod
    def get_service():
        return build('youtube', 'v3', developerKey=Channel.API_KEY)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    def to_json(self, name_file):
        with open(name_file, "a") as file:
            file.write(f'{self.__channel_id}\n{self.title}\n')