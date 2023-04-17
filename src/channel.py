import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

#import isodate
#from helper.youtube_api_manual import youtube
api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.subscribers = self.channel["items"][0]["statistics"]["subscriberCount"]
        print(f'''{self.channel_id} 
        {self.channel}
        {self.title}
        {self.url}
        {self.video_count}
        {self.subscribers}''')

    def __str__(self):
        return f"{self.title} {(self.url)}"

    def print_info(self, channel: dict) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def get_service(cls):
        return cls.youtube

    def to_json(self, __init__):
        return json.dumps(__init__, indent=2, ensure_ascii=False)

    def __add__(self, other):
        if type(other) == Channel:
            return int(self.subscribers) + int(other.subscribers)
        else:
            raise TypeError

    def __sub__(self, other):
        return int(other.subscribers) - int(self.subscribers)

    def __sub__(self, other):
        return int(self.subscribers) - int(other.subscribers)

    def __lt__(self, other):
        return int(self.subscribers) < int(other.subscribers)
    def __le__(self, other):
        return int(self.subscribers) <= int(other.subscribers)

    def __gt__(self, other):
        return int(self.subscribers) > int(other.subscribers)

    def __ge__(self, other):
        return int(self.subscribers) >= int(other.subscribers)
