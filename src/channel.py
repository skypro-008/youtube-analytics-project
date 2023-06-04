import json
import os

from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id: str = channel_id #id канала
        channel = self._get_channel_info()
        self.title: str = channel['items'][0]['snippet']['title'] #название канала
        self.description: str = channel['items'][0]['snippet']['description'] #описание канала
        self.url: str =f'https://www.youtube.com/channel/{channel["items"][0]["id"]}' #ссылка на канал
        self.subscriber_count: int = channel['items'][0]['statistics']['subscriberCount'] #количество подписчиков
        self.video_count: int = channel['items'][0]['statistics']['videoCount'] #количество видео
        self.view_count: int = channel['items'][0]['statistics']['viewCount'] #общее количество просмотров

    def _get_channel_info(self):
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.channel = self._get_channel_info()
        return json.dump(channel, indent=2, ensure_ascii=False)


    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')  # Получен токен
        youtube = build('youtube', 'v3', developerKey=api_key)  # Специальный объект для работы с API
        return youtube

    # Геттер для channel_id
    @property
    def channel_id(self):
        return channel_id

    def to_json(self, filename):
        with open(filename, "w", encoding='utf-8') as file:
            channel_info = {
                            "channel_id": self.__channel_id,
                            "title": self.title,
                            "description": self.description,
                            "url": self.url,
                            "subscriberCount": self.subscriber_count,
                            "videoCount": self.video_count,
                            "viewCount": self.view_count
                            }
            json.dump(channel_info, file, indent=2, ensure_ascii=False)
