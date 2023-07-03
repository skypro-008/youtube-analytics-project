import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YUOTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]
        self.url = 'https://www.youtube.com/channel/' + channel_id
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.subsc_count = channel['items'][0]['statistics']['subscriberCount']
        self.view = channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return int(self.subsc_count) + int(other.subsc_count)

    def __sub__(self, other):
        return int(self.subsc_count) - int(other.subsc_count)

    def __lt__(self, other):
        return int(self.subsc_count) < int(other.subsc_count)

    def __le__(self, other):
        return int(self.subsc_count) <= int(other.subsc_count)

    def __gt__(self, other):
        return int(self.subsc_count) > int(other.subsc_count)

    def __ge__(self, other):
        return int(self.subsc_count) >= int(other.subsc_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, name_ile: str):
        """Сохраняет в файл значения атрибутов экземпляра `Channel`
           подсмотренно на сайте https://sky.pro/media/modul-json-v-python/"""
        result = self.__dict__
        result["Channel"] = self.__class__.__name__
        with open(name_ile, "w", encoding="utf8") as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

    @property
    def name(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        service_tube = build('youtube', 'v3', developerKey=api_key)
        return service_tube
