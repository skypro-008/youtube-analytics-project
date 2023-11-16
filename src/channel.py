import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    # YOUT_API_KEY скопирован из гугла и вставлен в переменные окружения
    API_KEY: str = os.getenv('YOUT_API_KEY')
    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)
