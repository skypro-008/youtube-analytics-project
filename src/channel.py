import json
import os

from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id: str = channel_id #id канала
        self.video_title: str = channel['items'][0]['snippet']['title'] #название канала
        self.desription: str = channel['items'][0]['snippet']['desription'] #описание канала
        self.url: str = channel['items'][0]['snippet']['url'] #ссылка на канал
        self.subscriber_count: int = channel['items'][0]['statistics']['subscriberCount'] #количество подписчиков
        self.video_count: int = channel['items'][0]['statistics']['videoCount'] #количество видео
        self.view_count: int = channel['items'][0]['statistics']['viewCount'] #общее количество просмотров


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        #channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # HighLoad Channel
        api_key: str = os.getenv('YT_API_KEY')  # Получен токен
        youtube = build('youtube', 'v3', developerKey=api_key)  # Специальный объект для работы с API
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    @classmethod
    def get_service(cls):
        return youtube

    def to_json(self, filename):
        with open(filename, "w", encoding='utf-8') as file:
            channel_info = {
                            "channel_id": self.channel_id,
                            "title": self.video_title,
                            "desription": self.desription,
                            "url": self.url,
                            "subscriberCount": self.subscriber_count,
                            "videoCount": self.video_count,
                            "viewCount": self.view_count
                            }
            json.dumps(channel_info, indent=2, ensure_ascii=False)
