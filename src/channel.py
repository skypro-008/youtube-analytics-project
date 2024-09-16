import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.subscriber_count = int(channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """возможность складывать"""
        result = self.subscriber_count + other.subscriber_count
        return result

    def __sub__(self, other):
        """возможность вычитать"""
        result = self.subscriber_count - other.subscriber_count
        return result

    def __gt__(self, other):
        """возможность сравнивать"""
        result = self.subscriber_count > other.subscriber_count
        return result

    def __ge__(self, other):
        """возможность сравнивать"""
        result = self.subscriber_count >= other.subscriber_count
        return result

    def __lt__(self, other):
        """возможность сравнивать"""
        result = self.subscriber_count < other.subscriber_count
        return result

    def printj(self, dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        self.info = (json.dumps(dict_to_print, indent=2, ensure_ascii=False))
        print(self.info)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.printj(channel)

    def to_json(self, file_name):
        channel_info = {"channel_id": self.channel_id, "title": self.title, "description": self.description,
                        "url": self.url, "subscriber_count": self.subscriber_count, "video_count": self.video_count,
                        "view_count": self.view_count}
        with open(file_name, "w", encoding='UTF-8') as file:
            json.dump(channel_info, file)

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YOUTUBE_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
