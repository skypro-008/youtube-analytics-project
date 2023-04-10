import json
import os
import isodate
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

api_key: str = 'AIzaSyB5hhIW1yHBoo4ZoayTT0Wi4hMqhWeos9c'

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id  # id-канала
        self._title = ""  # название канала
        self._description = ""  # описание канала
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"  # ссылка на канал
        self._subscriber_count = ""  # количество подписчиков
        self._video_count = ""  # количество видеороликов
        self._view_count = ""  # количество просмотров

    def channel_id(self):
        return self.__channel_id


    @property
    def title(self):
        self.print_info1()
        return self.channel_id

    @property
    def video_count(self):
        return self._video_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)

    def print_info1(self):
        apikey: str = os.getenv('YT_API_KEY')
        ytube = build('youtube', 'v3', developerKey=apikey)
        channel = ytube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self._title = channel["items"][0]['snippet']['title']
        self._video_count = channel["items"][0]['statistics']['videoCount']

    """
    возвращает объект для работы с YouTube API
    """
    @classmethod
    def get_service(cls):
        apikey: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=apikey)

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


