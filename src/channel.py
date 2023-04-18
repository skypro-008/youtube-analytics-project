import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        channel_data = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.id = channel_data['items'][0]['id']
        self.title = channel_data['items'][0]['snippet']['title']
        self.description = channel_data['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.id}"
        self.subscriber_count = int(channel_data['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(channel_data['items'][0]['statistics']['videoCount'])
        self.view_count = int(channel_data['items'][0]['statistics']['viewCount'])

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        return youtube

    def to_json(self, file_path: str) -> None:
        """Сохраняет в файл значения атрибутов экземпляра Channel."""
        with open(file_path, 'w') as file:
            json.dump(self.__dict__, file, ensure_ascii=False, indent=4)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
