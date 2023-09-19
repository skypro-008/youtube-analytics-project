import json
import os
from googleapiclient.discovery import build
import isodate

class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.info = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = channel_id
        self.title = self.info['items'][0]['snippet']['title']
        self.description = self.info['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.subscriber_count = self.info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.info['items'][0]['statistics']['videoCount']
        self.view_count = self.info['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id


    @staticmethod
    def get_service():
        return Channel.youtube

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.info, indent=2, ensure_ascii=False))

    def to_json(self,pach_):
        '''метод сохраняющий в файл значения атрибутов экземпляра Channel'''

        data = {}
        data['channel_id'] = self.__channel_id
        data['title'] = self.title
        data['description'] = self.description
        data['url'] = self.url
        data['subscriber_count'] = self.subscriber_count
        data['video_count'] = self.video_count
        data['view_count'] = self.view_count
        with open(pach_, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

