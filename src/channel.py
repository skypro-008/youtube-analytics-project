import json
import os

from googleapiclient.discovery import build

API_KEY: str = os.getenv('YT_API_KEY')

youtube = googleapiclient('youtube', 'v3', developerKey=API_KEY)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API"""
        self.channel_id = channel_id


    def print_json(self, dict_print: dict) -> None:
        """Выводит словарь в json-подобном формате с отступами"""
        print(json.dumps(dict_print, indent=2, ensure_ascii=False))


    def get_channel_id(self):
        """Получить данные о канале по его id"""
        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id).execute()
        return channel


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        channel = self.get_channel_id()
        channel_json = channel.print_json()
        print(channel_json)
