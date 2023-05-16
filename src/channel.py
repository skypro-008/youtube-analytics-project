import json
import os
from googleapiclient.discovery import build

API_KEY: str = os.getenv('YT_API_KEY')
YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)


class Channel:
    """
    Класс для ютуб-канала
    """


    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.channel = YOUTUBE.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = channel_id
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']


    def __str__(self):
        return f'{self.title} ({self.url})'


    def __add__(self, other):
        return self.int_subscriber_count + other.int_subscriber_count


    def __sub__(self, other):
        return self.int_subscriber_count - other.int_subscriber_count


    def __lt__(self, other):
        return self.int_subscriber_count < other.int_subscriber_count


    def __le__(self, other):
        return self.int_subscriber_count <= other.int_subscriber_count


    def __gt__(self, other):
        return self.int_subscriber_count > other.int_subscriber_count


    def __ge__(self, other):
        return self.int_subscriber_count >= other.int_subscriber_count


    def __eq__(self, other):
        return self.int_subscriber_count == other.int_subscriber_count


    @property
    def int_subscriber_count(self):
        """
        Возвращает число из строки (для сравнения)

        :return: число int
        """
        return int(self.subscriber_count)


    @property
    def channel_id(self) -> str:
        """
        Геттер, возвращает id канала
        return: id канала
        """
        return self.__channel_id


    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


    @staticmethod
    def get_service() -> object:
        """
        Возвращает объект для работы с YouTube API
        return: объект для работы с YouTube API
        """
        return YOUTUBE


    def to_json(self, path) -> None:
        """
        Записывает аттрибуты экземпляра в json
        param: путь к файлу
        """
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
