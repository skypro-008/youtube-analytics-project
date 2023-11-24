import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    # YOUT_API_KEY скопирован из гугла и вставлен в переменные окружения
    API_KEY: str = os.getenv('YOUT_API_KEY')
    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str, title=None, channel_description=None, url=None,
                 number_of_subscribers=None, video_count=None, total_number_views=None) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.channel_description = channel['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + str(channel_id)
        self.number_of_subscribers = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.total_number_views = channel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, filename):
        """Сохраняет в файл значения атрибутов экземпляра `Channel`"""
        data = {
            'id_канала': self.channel_id,
            'название канала': self.title,
            'описание канала': self.channel_description,
            'ссылка на канал': self.url,
            'количество подписчиков': self.number_of_subscribers,
            'количество видео': self.video_count,
            'общее количество просмотров': self.total_number_views
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)
