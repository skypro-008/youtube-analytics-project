import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    @classmethod
    def get_service(cls):
        __API_KEY = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=__API_KEY)
        return youtube

    @property
    def title(self):
        title = self.print_info()
        return title['items'][0]['snippet']['title']

    @property
    def video_count(self):
        video_count = self.print_info()
        return video_count['items'][0]['statistics']['videoCount']

    @property
    def url(self):
        return f'https://www.youtube.com/channel/{self.channel_id}'

    def to_json(self, dict_to_print) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        __API_KEY = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=__API_KEY)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel
