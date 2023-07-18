import json
import os

from googleapiclient import discovery
# from googleapiclient.discovery import build

API_KEY = os.getenv("YT_API_KEY")
# API_KEY: str = os.getenv("YT_API_KEY")
api_service_name = "youtube"
api_version = "v3"

youtube = discovery.build(api_service_name, api_version, developerKey=API_KEY)
# youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=API_KEY)

url_main_channel = 'https://www.youtube.com/channel/'


class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API
        """
        self.channel_id = channel_id
        self.title: str = self.get_channel_id()['items'][0]['snippet']['title']
        self.description: str = self.get_channel_id()['items'][0]['snippet']['description']
        self.url: str = url_main_channel + channel_id
        self.subscriberCount: int = self.to_int(self.get_channel_id()['items'][0]['statistics']['subscriberCount'])
        self.videoCount: int = self.get_channel_id()['items'][0]['statistics']['videoCount']
        self.viewCount: int = self.get_channel_id()['items'][0]['statistics']['viewCount']


    def __str__(self):
        return f'{self.title}({self.url})'


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


    def to_int(self, numb):
        """Возвращает полученное значение в типе int"""
        if type(numb) == int:
            return numb
        else:
            num_int = int(float(numb))
            return num_int


    def print_json(self, dict_print: dict) -> None:
        """Выводит словарь в json-подобном формате с отступами"""
        print(json.dumps(dict_print, indent=2, ensure_ascii=False))


    def get_channel_id(self):
        """Получить данные о канале по его id"""
        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return channel


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        channel = self.get_channel_id()
        self.print_json(channel)


    @classmethod
    def get_service(cls):
        """
        Класс-метод `get_service()` возвращает объект для работы с YouTube API
        """
        youtube = discovery.build(api_service_name, api_version, developerKey=API_KEY)
        return youtube


    def to_json(self, file_name: str):
        """
        Метод `to_json()` сохраняет в файл значения атрибутов экземпляра `Channel`
        """
        data = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file)
