import json
import os
from googleapiclient.discovery import build

class Channel:

    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info["items"][0]["snippet"]['title']
        self.description = self.channel_info["items"][0]["snippet"]['description']
        self.url = "https://www.youtube.com/channel/" + f"{channel_id}"
        self.video_count = self.channel_info["items"][0]["statistics"]["videoCount"]

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь
        channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    @classmethod
    def get_service(cls):
        """Класс-метод возвращающий объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, file_json):
        f"""Сохраняет данные о канале в файл {file_json}.json в формате .json"""
        data = {"api_key": Channel.api_key,
                "channel_id": self.channel_id,
                "title:": self.title,
                "description": self.description,
                "url": self.url,
                "video_count": self.video_count}
        data = json.dumps(data)
        my_file = open(f"{file_json}", "w+")
        my_file.write(data)
        my_file.close()



