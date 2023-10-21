import os
import json

from googleapiclient.discovery import build

env_var=os.environ
env_var['YT_API_KEY'] = 'AIzaSyB1z7KSI8FjqZqYXqTWN2424WwijUQrzIs'
class Channel:
    """Класс для ютуб-канала"""

    API_KEY = os.getenv("YT_API_KEY")
    YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = None
        self.description = None
        self.url = None
        self.subscribers = None
        self.video_count = None
        self.view_count = None

        api_key: str = os.getenv('YT_API_KEY')

        youtube = self.get_service(api_key)
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=self.channel_id
        )

        response = request.execute()
        if response['items']:
            channel_data = response['items'][0]
            self.title = channel_data['snippet']['title']
            self.description = channel_data['snippet']['description']
            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
            self.subscribers = int(channel_data['statistics']['subscriberCount'])
            self.video_count = int(channel_data['statistics']['videoCount'])
            self.view_count = int(channel_data['statistics']['viewCount'])

    def __str__(self):
        '''возвращает название и ссылку на канал'''
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        '''складывание двух каналов между собой по количеству подписчиков'''
        return self.subscribers + other.subscribers

    def __sub__(self, other):
        '''вычитание двух каналов между собой по количеству подписчиков'''
        return self.subscribers - other.subscribers

    def __gt__(self, other):
        '''сравнение «больше» > двух каналов между собой по количеству подписчиков'''
        return self.subscribers > other.subscribers

    def __ge__(self, other):
        '''сравнение «больше или равно» >= двух каналов между собой по количеству подписчиков '''
        return self.subscribers >= other.subscribers

    def __lt__(self, other):
        '''сравнение «меньше» < двух каналов между собой по количеству подписчиков '''
        return self.subscribers < other.subscribers

    def __le__(self, other):
        '''сравнение «меньше или равно»  <= двух каналов между собой по количеству подписчиков '''
        return self.subscribers <= other.subscribers

    def __eq__(self, other):
        '''сравнение  "равенство" == двух каналов между собой по количеству подписчиков '''
        return self.subscribers == other.subscribers

    def print_info(self) -> None:

        channel = self.YOUTUBE.channels().list(id=self.id,  part='snippet,statistics').execute() # в этой строчке обратичлся через self к аргумeнту YOUTUBE
        print(json.dumps(channel, indent=2)) # в этой строчке распокавал ответ с помощью библиотеки json

    @classmethod
    def get_service(cls, api_key: str):
        """Возвращает объект для работы с YouTube API."""
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename: str) -> None:
        """Сохраняет в файл значения атрибутов экземпляра Channel в формате JSON."""
        data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscribers": self.subscribers,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
        with open(filename, 'w') as f:
            json.dump(data, f)