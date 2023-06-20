import json
import os
from googleapiclient.discovery import build
import isodate

#Неработает os.getenv('YT_API_KEY')
api_key: str = 'AIzaSyBNte6ggcZnydJxTP7W0H8olVEGbfJnMcY'
youtube = build('youtube', 'v3', developerKey=api_key)
# channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return self.printj(channel)
    #Задел на будующее
    #def printj(self, dict_to_print) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        #print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

