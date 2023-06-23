import json
import os

from googleapiclient.discovery import build

api_key: str = os.getenv('YOUTUBE_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""

        self.id = channel_id
        self.object = self.get_service()
        self.info = self.object.channels().list(id=self.id, part='snippet,statistics').execute()
        self.title = self.info['items'][0]['snippet']['title']
        self.description = self.info['items'][0]['snippet']['description']
        self.url = os.path.join('https://www.youtube.com/channel/', self.id)
        self.subscribers = self.info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.info['items'][0]['statistics']['videoCount']
        self.views = self.info['items'][0]['statistics']['viewCount']

    def __str__(self) -> str:
        """Возвращает инфо в формате '<название_канала> (<ссылка_на_канал>)'"""
        return f'{self.title} ({self.url})'

    def __add__(self, other) -> int:
        """Возвращает суммарное кол-во подписчиков двух каналов"""
        return int(self.subscribers) + int(other.subscribers)

    def __sub__(self, other) -> int:
        """Возвращает кол-во подписчиков первого канала минус кол-во подписчиков второго канала"""
        return int(self.subscribers) - int(other.subscribers)

    def __lt__(self, other) -> bool:
        '''Проверяет кол-во подписчиков первого канала < второго канала'''
        return int(self.subscribers) < int(other.subscribers)

    def __le__(self, other) -> bool:
        '''Проверяет кол-во подписчиков первого канала <= второго канала'''
        return int(self.subscribers) <= int(other.subscribers)

    def __gt__(self, other) -> bool:
        '''Проверяет кол-во подписчиков первого канала > второго канала'''
        return int(self.subscribers) > int(other.subscribers)

    def __ge__(self, other) -> bool:
        '''Проверяет кол-во подписчиков первого канала >= второго канала'''
        return int(self.subscribers) >= int(other.subscribers)

    def __eq__(self, other) -> bool:
        '''Проверяет кол-во подписчиков первого канала == второго канала'''
        return int(self.subscribers) == int(other.subscribers)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращает объект для работы с YouTube API."""

        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, file):
        """Сохраняет/добавляет в файл значения атрибутов экземпляра Channel."""

        data = {"id канала": self.id,
                "название канала": self.title,
                "описание канала": self.description.strip(),
                "ссылка на канал": self.url,
                "количество подписчиков": self.subscribers,
                "количество видео": self.video_count,
                "общее количество просмотров": self.views
                }
        with open(file, 'a', encoding='utf-8') as f:
            if os.stat(file).st_size == 0:
                json.dump([data], f, ensure_ascii=False)
            else:
                with open(file, 'r', encoding='utf-8') as f:
                    channels_list = json.load(f)
                    channels_list.append(data)
                with open(file, 'w', encoding='utf-8') as f:
                    json.dump(channels_list, f, ensure_ascii=False)
