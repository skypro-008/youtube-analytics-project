import json
import os
from googleapiclient.discovery import build


YT_API_KEY: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id =  channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        channel = youtube.channels().list(id=self.channel_id,
                                          part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

