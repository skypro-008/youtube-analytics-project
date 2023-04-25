import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id
        self.channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.channel_info["items"][0]["id"]}'
        self.subs = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.views = self.channel_info['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel_info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Dозвращает объект для работы с YouTube API"""

        return cls.youtube

    def to_json(self, filename):
        """Cохраняет в файл значения атрибутов экземпляра `Channel`"""

        with open(filename, 'w', encoding="utf-8") as outfile:
            json.dump(self.channel_info, outfile, indent=2, ensure_ascii=False)
