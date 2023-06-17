from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютубканала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные
        будут подтягиваться по API."""

        api_key: str = os.getenv('YouTube_API')
        youtube = build('youtube', 'v3', developerKey = api_key)
        partfk = 'snippet,statistics'
        ytbefk = youtube.channels()
        self.channel_id = ytbefk.list(id = channel_id, part = partfk).execute()


    def printj(self, dict_to_print: dict) -> None:
        """Выводит словарь в json - подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent = 2, ensure_ascii = False))


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        return self.printj(self.channel_id)
