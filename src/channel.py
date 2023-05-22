import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = Channel.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        # новые атрибуты
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']["default"]['url']
        self.subscriberCount = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.viewCount = channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = Channel.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel_info = json.dumps(channel, indent=2, ensure_ascii=False)
        print(channel_info)

    @classmethod
    def get_service(cls):
        """Класс-метод возвращающий объект для работы с YouTube API"""
        api_key: str = os.getenv('YT_API_KEY')
        object_get = build('youtube', 'v3', developerKey=api_key)
        return object_get

    def to_json(self, file_name):
        """Мохраняющий в файл значения атрибутов экземпляра `Channel`"""
        dict_hw_2 = {}
        dict_hw_2['id'] = self.channel_id
        dict_hw_2['title'] = self.title
        dict_hw_2['description'] = self.description
        dict_hw_2['url'] = self.url
        dict_hw_2['subscriberCount'] = self.subscriberCount
        dict_hw_2['video_count'] = self.video_count
        dict_hw_2['viewCount'] = self.viewCount

        with open(file_name, 'w') as f:
            json.dump(dict_hw_2, f, indent=2)

    @property
    def channel_id(self) -> str:
        # геттер для закрытого атрибута channel_id
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        # сеттер для закрытого атрибута channel_id
        self.__channel_id = channel_id
