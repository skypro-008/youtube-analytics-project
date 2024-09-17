import json
from src.get_service import *


class Channel(Get_Service):

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        CHANNEL_INFO = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title: str = CHANNEL_INFO['items'][0]['snippet']['title']
        self.description: str = CHANNEL_INFO['items'][0]['snippet']['description']
        self.url: str = f'https://www.youtube.com/channel/{CHANNEL_INFO["items"][0]["id"]}'
        self.subscribe_count: int = CHANNEL_INFO['items'][0]['statistics']['subscriberCount']
        self.video_count: int = CHANNEL_INFO['items'][0]['statistics']['videoCount']
        self.view_count: int = CHANNEL_INFO['items'][0]['statistics']['viewCount']

    @classmethod
    def get_service(cls):
        return cls.youtube

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        dict_channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(dict_channel_info, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        template = {
            'id_канала': self.channel_id,
            'название_канала': self.title,
            'описание_канала': self.description,
            'ссылка_на_канал': self.url,
            'количество_подписчиков': self.subscribe_count,
            'количество_видео': self.video_count,
            'общее_количество_просмотров': self.view_count
        }
        with open(file_name, 'w') as file:
            json.dump(template, file, indent=1, ensure_ascii=False)

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other) -> int:
        return self.subscribe_count + other.subscribe_count

    def __sub__(self, other) -> int:
        return int(self.subscribe_count) - int(other.subscribe_count)

    def __gt__(self, other) -> bool:
        return self.subscribe_count > other.subscribe_count

    def __ge__(self, other) -> bool:
        return self.subscribe_count >= other.subscribe_count

    def __lt__(self, other) -> bool:
        return self.subscribe_count < other.subscribe_count

    def __le__(self, other) -> bool:
        return self.subscribe_count <= other.subscribe_count

    def __eq__(self, other) -> bool:
        return self.subscribe_count == other.subscribe_count


