import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        API_KEY = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)
