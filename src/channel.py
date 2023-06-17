from googleapiclient.discovery import build
import os
import json

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        #self.channel_id = channel_id
        api_key: str = os.getenv('YouTube_API')
        youtube = build('youtube', 'v3', developerKey=api_key)
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    def printj(self,dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:

        """Выводит в консоль информацию о канале."""
        return self.printj(self.channel_id)

