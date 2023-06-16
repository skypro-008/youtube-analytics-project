import json
import os

from googleapiclient.discovery import build
from pprint import pprint

class Channel:
    """Класс для ютуб-канала"""
    #api_key: str = os.getenv('YT_API_KEY')
    api_key = "AIzaSyAA_DGWlyk07XTfwlz507KCFoh2Q8AeM5Y"
    youtube = build('youtube', 'v3', developerKey=api_key)


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        #youtube = build('youtube', 'v3', developerKey=self.api_key)
        input_dict = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        pprint(input_dict)
        self.title = input_dict['items'][0]['snippet']['title']
        self.description = input_dict['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.subscribers = input_dict['items'][0]['statistics']['subscriberCount']
        self.video_count = input_dict['items'][0]['statistics']['videoCount']
        self.view = input_dict['items'][0]['statistics']['viewCount']


    def __str__(self):
        return f'{self.title}({self.url}'

    def __add__(self, other):
        return self.subscribers + other.subscribers


    def __sub__(self, other):
        return int(self.subscribers - other.subscribers)

    def __eq__(self, other):
        return self.subscribers == other.subscribers


    def __lt__(self, other):
        return self.subscribers < other.subscribers


    def __gt__(self, other):
        return self.subscribers > other.subscribers


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute(), indent=2, ensure_ascii=False))


    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    @property
    def channel_id(self):
        return self.__channel_id


    def to_json(self, path):
        with open (path, "w") as file:
            file.write(json.dumps(self.__dict__, indent=2))

n = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
print(n.title)
n.to_json("tex.txt")



