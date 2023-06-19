from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютубканала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала и т.д.. Дальше все данные
        будут подтягиваться по API."""

        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YouTube_API')

        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.__channel_id = channel_id #id канала
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()




        self.title =self.channel['items'][0]['snippet']['title'] # название канала
        self.description =self.channel['items'][0]['snippet']['description']#описание канала
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']  #ссылка на канал
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount'] #количество подписчиков
        self.view_count = self.channel['items'][0]['statistics']['viewCount']#количество просмотров
        self.video_count = self.channel['items'][0]['statistics']['videoCount']  # общее количество просмотров


    def printj(self, dict_to_print: dict) -> None:
        """Выводит словарь в json - подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent = 2, ensure_ascii = False))


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        return self.printj(self.channel_id)

    @classmethod
    def get_service(cls):
        """метод возвращает объект для работы с YouTube API"""
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YouTube_API')
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return cls(youtube)

    @property
    def channel_id(self):
        """свойство скрытия атрибута ид канала"""
        return self.__channel_id

    def to_json(self):
        """метод сохраняющий в файл значения атрибутов экземпляра Channel"""
        dict = {
            "channel_id": self.__channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.subscriber_count,
            "viewCount": self.view_count,
            "videoCount" : self.video_count

        }
        with open("moscowpython.json", "w") as file_json:
            json.dump(dict, file_json)



