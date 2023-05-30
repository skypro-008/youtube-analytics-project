import os
import json
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
class Channel:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = None
        self.description = None
        self.url = None
        self.count_subscriber = None
        self.video_count = None
        self.all_count_views = None

        self.response = Channel.youtube.channels().list(
            part='snippet,contentDetails,statistics',
            id=channel_id
        ).execute()


        # Обработка полученного результата
        channel_items = self.response['items'][0]
        snippet = channel_items['snippet']
        statistics = channel_items['statistics']

        self.title = snippet['title']
        self.description = snippet['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.count_subscriber = int(statistics['subscriberCount'])
        self.video_count = statistics["videoCount"]
        self.all_count_views = statistics['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.count_subscriber + other.count_subscriber


    def __sub__(self, other):
        return self.count_subscriber - other.count_subscriber


    def __gt__(self, other):
        return self.count_subscriber > other.count_subscriber

    def __ge__(self, other):
        return self.count_subscriber >= other.count_subscriber

    def __lt__(self, other):
        return self.count_subscriber < other.count_subscriber

    def __le__(self, other):
        return self.count_subscriber <= other.count_subscriber


    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, file_name):
        data = {'channel.id': self.__channel_id,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'count_subscriber': self.count_subscriber,
                'all_count_views': self.all_count_views
                }
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # Вывод результатов
        print(json.dumps(self.response, indent=2, ensure_ascii=False))

# moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
# highload = Channel('UCwHL6WHUarjGfUM_586me8w')
# print(moscowpython)
# print(moscowpython + highload)
# print(moscowpython - highload)
# print(highload - moscowpython)
# print(moscowpython > highload)
# print(moscowpython >= highload)
# print(moscowpython < highload)
# print(moscowpython <= highload)
# print(moscowpython == highload)
