import json
import os
from googleapiclient.discovery import build
import isodate

api_key = 'AIzaSyDoXfDhCmEBqP323Mfo599sILGCvB9-Gb4'
#пришлось выключить, пока что не подтягивает эту переменную, хотя через консоль ее нахожу
#api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.id = self.channel['items'][0]['id']
        self.title = self.channel['items'][0]['snippet']['title']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.description = self.channel['items'][0]['snippet']['description']
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']
        self.subscriberCount = self.channel['items'][0]['statistics']['subscriberCount']


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
    @classmethod
    def get_service(cls):
        return youtube
    def to_json(self, name):
        with open(name, "w") as file:
            file.write(str(vars(self)))


