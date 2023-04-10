import json
import os
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build
import isodate


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self._title = ""
        self._description = ""
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self._subscriber_count = ""
        self._video_count = ""
        self._view_count = ""

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        """Название канала в виде переменной, плюс проверка"""
        self.print_info1()
        return self.channel_id

    @property
    def video_count(self):
        return self._video_count

    def print_info(self):
        """Выводит информацию о канале"""
        api_key: str = os.getenv('YT_API_KEY')
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        printj = json.dumps(channel, indent=2, ensure_ascii=False)
        return print(printj)

    def print_info1(self):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self._title = channel["items"][0]['snippet']['title']
        self._video_count = channel["items"][0]['statistics']['videoCount']

        """get_service возвращает объект для работы с YouTube API """
    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        """Создание файла json из атрибутов класса"""
        data = {
            "channel_id": self.__channel_id,
            "title": self.title,
            "description": self._description,
            "url": self.url,
            "subscriber_count": self._subscriber_count,
            "video_count": self._video_count,
            "view_count": self._view_count
        }
        with open(filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)