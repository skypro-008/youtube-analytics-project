import os
import json

from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    AAPI_KEY = os.getenv("YT_API_KEY")
    YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.id = channel_id

    def print_info(self) -> None:

        channel = self.YOUTUBE.channels().list(id=self.id,  part='snippet,statistics').execute(). # в этой строчке обратичлся через self к аргумeнту YOUTUBE
        print(json.dumps(channel, indent=2)) # в этой строчке распокавал ответ с помощью библиотеки json
