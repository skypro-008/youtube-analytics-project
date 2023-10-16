import os
import json
from googleapiclient.discovery import build


class Channel:

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key = os.getenv('YouTubeAPI')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def print_info(self):
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))


