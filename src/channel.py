import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.__channel_id = channel_id
        self.title = None
        self.channel_description = None
        self.url = None
        self.num_subscribers = None
        self.video_count = None
        self.total_views = None
        self.__api_key = os.getenv('YT_API_KEY')
        self.get_channel_info()

        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

    def __str__(self):
        # название и ссылка на канал по шаблону <название_канала> (<ссылка_на_канал>)
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.video_count + other.video_count

    def __sub__(self, other):
        return self.video_count - other.video_count

    def __eq__(self, other):
        return self.video_count == other.video_count

    def __lt__(self, other):
        return self.video_count < other.video_count

    def __ge__(self, other):
        return self.video_count >= other.video_count

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        # объект для работы с YouTube API
        __api_key = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=__api_key)
        return youtube

    def get_channel_info(self):
        youtube = self.get_service()
        channel_data = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        if 'items' in channel_data:
            channel_data = channel_data['items'][0]
            self.title = channel_data['snippet']['title']
            self.channel_description = channel_data['snippet']['description']
            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
            self.num_subscribers = int(channel_data['statistics']['subscriberCount'])
            self.video_count = int(channel_data['statistics']['videoCount'])
            self.total_views = int(channel_data['statistics']['viewCount'])

    def to_json(self, filename):
        # сохраняет в файл '*.json' значения атрибутов экземпляра Channel
        channel_data = {
            'channel_id': self.channel_id,
            'channel_title': self.title,  # Corrected key name
            'channel_description': self.channel_description,
            'channel_link': self.url,
            'num_subscribers': self.num_subscribers,
            'num_videos': self.video_count,
            'total_views': self.total_views
        }
        with open(filename, 'w') as file:
            json.dump(channel_data, file)

    def print_info(self) -> None:
        # Выводит в консоль информацию о канале
        print(f"Channel ID: {self.channel_id}")
        print(f"Channel Name: {self.title}")
        print(f"Channel Description: {self.channel_description}")
        print(f"Channel Link: {self.url}")
        print(f"Number of Subscribers: {self.num_subscribers}")
        print(f"Number of Videos: {self.video_count}")
        print(f"Total Views: {self.total_views}")
