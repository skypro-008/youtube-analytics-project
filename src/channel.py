import json
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id  # HighLoad Channel
        self.channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['localized']['title']
        self.description = self.channel['items'][0]['snippet']['localized']['description']
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        self.subscriberCount = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.viewCount = int(self.channel['items'][0]['statistics']['viewCount'])

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other):
        return self.subscriberCount - other.subscriberCount

    def __gt__(self, other):
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other):
        return self.subscriberCount >= other.subscriberCount

    def __lt__(self, other):
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other):
        return self.subscriberCount <= other.subscriberCount

    def __eq__(self, other):
        return self.subscriberCount == other.subscriberCount

    @staticmethod
    def print_info() -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.dict, file, indent=4, ensure_ascii=False)
