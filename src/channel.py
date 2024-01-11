import os
import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber = self.channel['items'][0]['statistics']['subscriberCount']
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']
        self.description = self.channel['items'][0]['snippet']['description']

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey = cls.api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        """Метод, сохраняющий в файл значения атрибутов экземпляра"""
        channel_info = {}
        channel_info["title"] = self.title
        channel_info["description"] = self.description
        channel_info["url"] = self.url
        channel_info["video_count"] = self.video_count
        channel_info["viewCount"] = self.viewCount
        channel_info["subscriber"] = self.subscriber
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(json.dumps(channel_info, indent=2, ensure_ascii=False))
