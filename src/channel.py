import json
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv


load_dotenv()
class Channel:
    """
    Класс для ютуб-канала
    """
    api_key: str = os.getenv('YT_API_KEY')

    youtube = build('youtube', 'v3', developerKey = api_key)


    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.channel_id = channel_id


    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        channel = self.youtube.channels().list(id = self.channel_id, part = 'snippet,statistics').execute()
        print(channel)


    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent = 2, ensure_ascii = False))

