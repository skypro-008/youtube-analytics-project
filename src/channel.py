import json
import os
from googleapiclient.discovery import build



class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        #self.api_key: str = os.getenv('API_KEY')
        #self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.dict_to_print = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]['description']
        self.url = f"https://www.youtube.com/channel/{self.channel['items'][0]['id']}"
        self.subscriber_count = self.channel["items"][0]['statistics']['subscriberCount']
        self.video_count = self.channel["items"][0]['statistics']['videoCount']
        self.view_count = self.channel["items"][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.dict_to_print, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, id):
        raise AttributeError("Property 'channel_id' of 'Channel' object has no setter")

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API
        """
        return cls.youtube

    def to_json(self, path):
        """
        Функция, сохраняющая в файл значения атрибутов экземпляра channel
        """
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(self.__dict__, file, ensure_ascii=False)

