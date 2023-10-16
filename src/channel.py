import os
import json
from googleapiclient.discovery import build


class Channel:

    api_key: str = os.getenv('YouTubeAPI')
    youtube: object = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self):
        print(json.dumps(self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()))

# print(os.getenv('YouTubeAPI'))
# api_key: str = os.getenv('YouTubeAPI')
# youtube: object = build('youtube', 'v3', developerKey=api_key)
# print(type(youtube))
# print(api_key)


