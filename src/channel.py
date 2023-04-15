import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv("YT_API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriberCount = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']

    @property
    def _channel_id(self):
        return self.channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """получить объект для работы с API"""

        return cls.youtube

    def to_json(self, name: str):
        """создаем файл 'vdud.json' в данными по каналу"""

        data = {'channel_id': self.channel_id,
                'channel': self.channel,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'subscriberCount': self.subscriberCount,
                'video_count': self.video_count,
                'viewCount': self.viewCount}
        with open(name, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def __repr__(self):
        return f'{self.channel_id}'
