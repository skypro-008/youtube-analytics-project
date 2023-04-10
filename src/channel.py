from googleapiclient.discovery import build
import json
import os


class Channel:
    """Класс для ютуб-канала"""
    __api_key = os.getenv('YT_API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.__title = self.__channel['items'][0]['snippet']['title']
        self.__description = self.__channel['items'][0]['snippet']['description']
        self.__url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.__subscribers_count = int(self.__channel['items'][0]['statistics']['subscriberCount'])
        self.__video_count = int(self.__channel['items'][0]['statistics']['videoCount'])
        self.__views_count = int(self.__channel['items'][0]['statistics']['viewCount'])

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        """Возвращает id канала"""
        return self.__channel_id

    @property
    def title(self):
        """Возвращает название канала."""
        return self.__title

    @property
    def description(self):
        """Возвращает описание канала."""
        return self.__description

    @property
    def url(self):
        """Возвращает ссылку на канал."""
        return self.__url

    @property
    def subscribers_count(self):
        """Возвращает количество подписчиков."""
        return self.__subscribers_count

    @property
    def video_count(self):
        """Возвращает количество видео."""
        return self.__video_count

    @property
    def views_count(self) -> int:
        """Возвращает общее количество просмотров."""
        return self.__views_count

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API"""
        return cls.__youtube

    def to_json(self, filename):
        """Метод, сохраняющий в файл значения атрибутов экземпляра `Channel`"""
        data = {
            'channel_id': self.__channel_id,
            'title': self.__title,
            'description': self.__description,
            'url': self.__url,
            'subscribers_count': self.__subscribers_count,
            'video_count': self.__video_count,
            'views_count': self.__views_count
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def __str__(self):
        """
        Метод `__str__`, возвращающий название и ссылку
        на канал по шаблону `<название_канала> (<ссылка_на_канал>)
        """
        return f"{self.__title} ({self.__url})"

    def __add__(self, other):
        """Сложение двух каналов по количеству подписчиков."""
        return self.__subscribers_count + other.__subscribers_count

    def __sub__(self, other):
        """Вычитание двух каналов по количеству подписчиков."""
        return self.__subscribers_count - other.__subscribers_count

    def __gt__(self, other):
        """Сравнение двух каналов по количеству подписчиков"""
        return self.__subscribers_count > other.__subscribers_count

    def __ge__(self, other):
        """Сравнение двух каналов по количеству подписчиков"""
        return self.__subscribers_count >= other.__subscribers_count

    def __lt__(self, other):
        """Сравнение двух каналов по количеству подписчиков"""
        return self.__subscribers_count < other.__subscribers_count

    def __le__(self, other):
        """Сравнение двух каналов по количеству подписчиков"""
        return self.__subscribers_count <= other.__subscribers_count

    def __eq__(self, other):
        """Сравнение двух каналов по количеству подписчиков"""
        return self.__subscribers_count == other.__subscribers_count
