import json
import os
import isodate
import helper

from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:
    """
    Класс для ютуб-канала
    """


    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. 
        Дальше все данные будут подтягиваться по API.
        """
        self.channel_id = channel_id

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        helper.youtube_api_manual.printj(channel)
