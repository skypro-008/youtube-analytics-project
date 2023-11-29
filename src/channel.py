import json

import dotenv
from googleapiclient.discovery import build
import os

dotenv.load_dotenv()


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.environ.get('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала."""

        self._channel_id: str = channel_id
        self.youtube = self.get_service()
        channel_data = self.get_channel_data()

        self.id = channel_data['id']
        self.title = channel_data['snippet']['title']
        self.description = channel_data['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.id}'
        self.subscriber_count = int(channel_data['statistics']
                                    ['subscriberCount'])
        self.video_count = int(channel_data['statistics']['videoCount'])
        self.view_count = int(channel_data['statistics']['viewCount'])

    @property
    def channel_id(self):
        """Свойство для получения значения атрибута channel_id."""
        return self._channel_id

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        if not cls.api_key:
            raise ValueError("API key is missing.")
        return build("youtube", "v3", developerKey=cls.api_key)

    def get_channel_data(self):
        """Получает данные о канале с использованием YouTube API."""
        channel = self.youtube.channels().list(
            id=self.channel_id, part='snippet,statistics'
        ).execute()
        return channel['items'][0]

    def to_json(self, filename: str) -> None:
        """Сохраняет значения атрибутов в файл в формате JSON."""
        channel_data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }

        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(channel_data, json_file, indent=2, ensure_ascii=False)
