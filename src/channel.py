import json
import os
from googleapiclient.discovery import build
from src.utils import find_value


class Channel:
    """Класс для ютуб-канала"""

    service = "youtube"
    version = "v3"
    name_key = "API_KEY"

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется по id канала. Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        self.__title = None
        self.__description = None
        self.__url = None
        self.__subscribers_count = None
        self.__video_count = None
        self.__views_count = None

        self.set_atr()

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def url(self):
        return self.__url

    @property
    def subscribers_count(self):
        return self.__subscribers_count

    @property
    def video_count(self):
        return self.__video_count

    @property
    def views_count(self):
        return self.__views_count

    def get_info(self) -> dict:
        """Получает данные о канале по его id"""

        manager = self.get_service()

        channel = manager.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    def set_atr(self) -> None:
        """
        Устанавливает значения основных атрибутов объекта
        на основании полученных по id данных канала
        """

        channel = self.get_info()

        self.__title = find_value(channel, "title")
        self.__description = find_value(channel, "description")
        self.__url = find_value(channel, "url")
        self.__subscribers_count = find_value(channel, "subscriberCount")
        self.__video_count = find_value(channel, "videoCount")
        self.__views_count = find_value(channel, "viewCount")

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        # получаем данные о канале по его id
        channel = self.get_info()

        # выводит словарь в json-подобном удобном формате с отступами
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Создаёт специальный объект для работы с API"""

        # API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv(cls.name_key)

        manager = build(cls.service, cls.version, developerKey=api_key)
        return manager

    def get_attributes_dict(self) -> dict:
        return {"channel_id": self.channel_id,
                "title": self.title,
                "description": self.description,
                "url": self.url,
                "subscribers_count": self.subscribers_count,
                "video_count": self.video_count,
                "views_count": self.views_count
                }

    def to_json(self, file_name) -> None:
        """Записывает аттрибуты экземпляра класса в json-файл"""

        from_root = "homework-2", file_name
        to_root = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(to_root, *from_root)
        attributes = self.get_attributes_dict()

        with open(path, "w", encoding="UTF-8") as json_file:
            json.dump(attributes, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)
