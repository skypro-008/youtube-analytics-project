from src.youtube import youtube
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.info = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.id = channel_id
        self.title = self.info.get("items")[0].get("snippet").get("title")
        self.description = self.info.get("items")[0].get("snippet").get("description")
        self.url = "https://www.youtube.com/" + self.id
        self.subs_count = int(self.info.get("items")[0].get("statistics").get("subscriberCount"))
        self.video_count = int(self.info.get("items")[0].get("statistics").get("videoCount"))
        self.view_count = int(self.info.get("items")[0].get("statistics").get("viewCount"))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls) -> object:
        """
        Возвращает экземпляр класса build
        """
        return youtube

    def to_json(self, file_name: str):
        """
        Сохраняет входящие даные в файл типа json
        :param: data - данные для сохранения
        :param: file_name - имя файла хранилища
        :return: bool - удачно ли все прошло
        """
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subs_count': self.subs_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(file_name, 'w') as f:
            json.dump(data, f)

    def __str__(self) -> str:
        return f'{self.title} ({self.url})'

    def __add__(self, other) -> int | str:
        try:
            return self.subs_count + other.subs_count
        except (AttributeError, TypeError) as er:
            return f' {er}: Тип данных не подходит'

    def __sub__(self, other):
        return self.subs_count - other.subs_count

    def __gt__(self, other):
        return self.subs_count > other.subs_count

    def __ge__(self, other):
        return self.subs_count >= other.subs_count

    def __lt__(self, other):
        return self.subs_count < other.subs_count

    def __le__(self, other):
        return self.subs_count <= other.subs_count

    def __eq__(self, other):
        return self.subs_count == other.subs_count
