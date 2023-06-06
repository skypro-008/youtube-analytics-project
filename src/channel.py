import json
# import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    # api_key: str = os.getenv('YT_API_KEY')
    api_key: str = "AIzaSyBIE1Zoz-q-0QXM1H8hp3e_N9xnuT_9xfI"
    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        try:
            self.__parse()
        except Exception as e:
            print("Error:", str(e))

    def __str__(self):
        """"""
        return f'{self.__channel_id} ({self.url})'

    def __add__(self, other):
        """Метод для выполнения операции сложение (+) между двумя объектами типа `Channel`"""
        if isinstance(other, Channel):
            return int(self.subscriber_count) + int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        """ Метод для выполнения операции вычитание (-) между двумя объектами типа `Channel`"""
        if isinstance(other, Channel):
            return int(self.subscriber_count) - int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for -")

    def __lt__(self, other):
        """Метод для выполнения операции сравнения меньше (<) между двумя объектами типа `Channel`"""
        if isinstance(other, Channel):
            return int(self.subscriber_count) < int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for <")

    def __le__(self, other):
        """ Метод для выполнения операции меньше-равно (<=) между двумя объектами типа `Channel`"""
        if isinstance(other, Channel):
            return int(self.subscriber_count) <= int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for <=")

    def __gt__(self, other):
        """ Метод для выполнения операции больше (>) между двумя объектами типа `Channel`"""
        if isinstance(other, Channel):
            return int(self.subscriber_count) > int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for >")

    def __ge__(self, other):
        """ Метод для выполнения операции больше-равно (>=) между двумя объектами типа `Channel`"""
        if isinstance(other, Channel):
            return int(self.subscriber_count) >= int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for >=")

    def __eq__(self, other):
        """ Метод для выполнения операции равно (==) между двумя объектами типа `Channel`"""
        if isinstance(other, Channel):
            return int(self.subscriber_count) == int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for ==")

    def __parse(self):
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube

    def get_channel(self):
        """Возвращает объект channel"""
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        return channel

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        """Сохраняет в файл значения атрибутов экземпляра `Channel`"""

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.__dict__, file, ensure_ascii=False)
