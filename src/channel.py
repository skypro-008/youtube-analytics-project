import json
import os

from googleapiclient import discovery
# import googleapiclient.discovery
# from googleapiclient.discovery import build

API_KEY = os.getenv("YT_API_KEY")
# API_KEY: str = os.getenv("YT_API_KEY")
api_service_name = "youtube"
api_version = "v3"

youtube = discovery.build(api_service_name, api_version, developerKey=API_KEY)
# youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=API_KEY)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API
        """
        self.channel_id = channel_id


    def print_json(self, dict_print: dict) -> None:
        """Выводит словарь в json-подобном формате с отступами"""
        print(json.dumps(dict_print, indent=2, ensure_ascii=False))


    def get_channel_id(self):
        """Получить данные о канале по его id"""
        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return channel


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        channel = self.get_channel_id()
        self.print_json(channel)


    @classmethod
    def get_service(cls):
        """
        Класс-метод `get_service()` возвращает объект для работы с YouTube API
        """
        pass


    def to_json(self):
        """
        Метод `to_json()` сохраняет в файл значения атрибутов экземпляра `Channel`
        """
        pass
