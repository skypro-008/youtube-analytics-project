import json
import os
from googleapiclient.discovery import build

APY_KEY: str = os.getenv('API_KEY')

youtube = build('youtube', 'v3', developerKey=APY_KEY)

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
    #    print(f"id канала: {self.__channel_id}")
    #    print(f"Название канала: {self.title}")
    #    print(f"Описание канала: {self.description}")
    #    print(f"Ссылка на канал: {self.url}")
    #    print(f"Количество подписчиков: {self.subscriber_count}")
    #    print(f"Количество видео: {self.video_count}")
    #    print(f"Общее количество просмотров: {self.view_count}")
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        printj(channel)


    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=APY_KEY)

    def to_json(self, filename: str) -> None:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, indent=2, ensure_ascii=False)