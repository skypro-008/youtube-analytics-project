import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__api_key = os.getenv('API_KEY')
        self.__youtube = build('youtube', 'v3', developerKey=self.__api_key)
        self.__channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.__channel['items'][0]['snippet']['title']
        self.description = self.__channel['items'][0]['snippet']['description']
        self.video_count = self.__channel['items'][0]['statistics']['videoCount']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subscribers = self.__channel['items'][0]['statistics']['subscriberCount']
        self.viewCount = self.__channel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def api_key(self):
        return self.__api_key

    @classmethod
    def get_service(cls):
        __API_KEY = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=__API_KEY)
        return youtube

    def to_json(self, dict_to_print) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        dictionary = {1: self.title,
                      2: self.description,
                      3: self.video_count,
                      4: self.url,
                      5: self.subscribers,
                      6: self.viewCount}
        with open(dict_to_print, 'w') as outfile:
            outfile.write(json.dumps(dictionary, indent=2, ensure_ascii=False))

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        __API_KEY = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=__API_KEY)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel
