import json
import os
from googleapiclient.discovery import build
import isodate


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('API_KEY_YOUTUBE')
    chanel_info = []

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API и сохранятся в атрибуты."""
        self.__channel_id = channel_id
        """GET запрос по id канала с необходимыми параметрами о канале. Возвращает данные о канале в формате JSON """
        r = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        # r_json_str = (json.dumps(r))
        # r_json_dict = json.loads(r_json_str)
        # print(type(r_json_dict))
        # атрибуты экземпляра при инициализации
        self.title = r['items'][0]["snippet"]["title"]
        self.description = r['items'][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + self.channel_id
        self.subscriber_count = r['items'][0]["statistics"]["subscriberCount"]
        self.video_count = r['items'][0]["statistics"]["videoCount"]
        self.view_count = r['items'][0]["statistics"]["viewCount"]

    def __str__(self):
        return f'<{self.title}> (<{self.url}>)'

    def __add__(self, other):
        if not isinstance(other, (int, Channel)):
            raise ArithmeticError("Правый операнд должен быть int или Channel")
        variable_other = other
        if isinstance(other, Channel):
            variable_other = other.subscriber_count
        return int(self.subscriber_count) + int(variable_other)

    def __sub__(self, other):
        if not isinstance(other, (int, Channel)):
            raise ArithmeticError("Правый операнд должен быть int или Channel")
        variable_other = other
        if isinstance(other, Channel):
            variable_other = other.subscriber_count
        return int(self.subscriber_count) - int(variable_other)

    def __rsub__(self, other):
        return self - other

    def __gt__(self, other):
        if not isinstance(other, (int, Channel)):
            raise ArithmeticError("Правый операнд должен быть int или Channel")
        variable_other = other
        if isinstance(other, Channel):
            variable_other = other.subscriber_count
        if int(self.subscriber_count) > int(variable_other):
            return True
        else:
            return False

    def __ge__(self, other):
        if not isinstance(other, (int, Channel)):
            raise ArithmeticError("Правый операнд должен быть int или Channel")
        variable_other = other
        if isinstance(other, Channel):
            variable_other = other.subscriber_count
        if int(self.subscriber_count) >= int(variable_other):
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, (int, Channel)):
            raise ArithmeticError("Правый операнд должен быть int или Channel")
        variable_other = other
        if isinstance(other, Channel):
            variable_other = other.subscriber_count
        if int(self.subscriber_count) <= int(variable_other):
            return True
        else:
            return False

    def __le__(self, other):
        if not isinstance(other, (int, Channel)):
            raise ArithmeticError("Правый операнд должен быть int или Channel")
        variable_other = other
        if isinstance(other, Channel):
            variable_other = other.subscriber_count
        if int(self.subscriber_count) < int(variable_other):
            return True
        else:
            return False

    def __eq__(self, other):
        if not isinstance(other, (int, Channel)):
            raise ArithmeticError("Правый операнд должен быть int или Channel")
        variable_other = other
        if isinstance(other, Channel):
            variable_other = other.subscriber_count
        if int(self.subscriber_count) == int(variable_other):
            return True
        else:
            return False

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Подключение по API к youtube. Возвращает объект для работы с YouTube API"""
        servise = build('youtube', 'v3', developerKey=Channel.api_key)
        return servise

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.get_channel_info())

    def to_json(self):
        """Сохраняет значения атрибутов в файл json."""
        data = {"id": self.channel_id, "title": self.title, "description": self.description, "url": self.url,
                "subscriber_count": self.subscriber_count, "video_count": self.video_count,
                "view_count": self.view_count}
        with open('info_MoscowPython_yuitube.json', 'w') as file:
            json.dump(data, file, indent=3)
