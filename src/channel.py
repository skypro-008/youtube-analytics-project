import os

from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    API_KEY = os.getenv("YT_API_KEY")
    YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.id = id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = YOUTUBE.channels().list(id=self.id, part='snippet,statistics').execute()
        print(channel)
