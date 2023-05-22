import json
import os
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource
from src.utils import find_value
from functools import total_ordering


@total_ordering
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
    def channel_id(self) -> str:
        return self.__channel_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def url(self) -> str:
        return self.__url

    @property
    def subscribers_count(self) -> str:
        return self.__subscribers_count

    @property
    def video_count(self) -> str:
        return self.__video_count

    @property
    def views_count(self) -> str:
        return self.__views_count

    def __str__(self) -> str:
        """Возвращает строку в формате: `<название_канала> (<ссылка_на_канал>)`"""

        return f"{self.title} ({self.url})"

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
        self.__url = f'https://www.youtube.com/channel/{find_value(channel, "id")}'
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
    def get_service(cls) -> Resource:
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

    def to_json(self, file_name: str) -> None:
        """Записывает аттрибуты экземпляра класса в json-файл"""

        from_root = "homework-2", file_name
        to_root = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(to_root, *from_root)
        attributes = self.get_attributes_dict()

        with open(path, "w", encoding="UTF-8") as json_file:
            json.dump(attributes, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)

    def __add__(self, other) -> int | Exception:
        """
        Реализует возможность сложения объектов данного класса
        между собой по количеству подписчиков
        """

        if isinstance(other, Channel):
            return int(self.subscribers_count) + int(other.subscribers_count)
        else:
            raise TypeError("Операции между этими объектами невозможны")

    def __sub__(self, other) -> int | Exception:
        """
        Реализует возможность вычитания объектов данного класса
        между собой по количеству подписчиков
        """

        if isinstance(other, Channel):
            return int(self.subscribers_count) - int(other.subscribers_count)
        else:
            raise TypeError("Операции между этими объектами невозможны")

    def __eq__(self, other) -> bool | Exception:
        """
        Реализует возможность сравнения по знаку "==" объектов данного класса
        между собой по количеству подписчиков
        """

        if isinstance(other, Channel):
            return self.subscribers_count == other.subscribers_count
        else:
            raise TypeError("Операции между этими объектами невозможны")

    def __lt__(self, other) -> bool | Exception:
        """
        Реализует возможность сравнения по знаку "<" объектов данного класса
        между собой по количеству подписчиков
        """

        if isinstance(other, Channel):
            return self.subscribers_count < other.subscribers_count
        else:
            raise TypeError("Операции между этими объектами невозможны")
