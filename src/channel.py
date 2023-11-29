from googleapiclient.discovery import build
import json
import os
import dotenv

dotenv.load_dotenv()


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))
        self.description = self.youtube_load()["items"][0]["snippet"]["description"]
        self.title = self.youtube_load()["items"][0]["snippet"]["title"]
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        self.count_subscribers = self.youtube_load()["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.youtube_load()["items"][0]["statistics"]["videoCount"]
        self.count_views = self.youtube_load()["items"][0]["statistics"]["viewCount"]

    def __str__(self):
        """
        возвращает название и ссылку на канал
        """
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """
        возвращает сумму подписчиков
        """
        return int(self.count_subscribers) + int(other.count_subscribers)

    def __sub__(self, other):
        """
        возвращает разность подписчиков
        """
        return int(self.count_subscribers) - int(other.count_subscribers)

    def __lt__(self, other):
        return int(self.count_subscribers) < int(other.count_subscribers)

    def __le__(self, other):
        return int(self.count_subscribers) <= int(other.count_subscribers)

    def youtube_load(self):
        """Выдает информацию о сайте"""
        channel = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print((json.dumps(self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute())))

    @classmethod
    def get_service(cls):
        """
        возвращает объект для работы с YouTube API
        """
        return build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))

    def to_json(self, filename):
        """
        сохраняет в файл значения атрибутов экземпляра Channel

        """
        channel_info = {"title": self.title,
                        "channel_id": self.__channel_id,
                        "description": self.description,
                        "url": self.url,
                        "count_podpishchikov": self.count_subscribers,
                        "video_count": self.video_count,
                        "count_views": self.count_views}
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(channel_info, file, indent=4, ensure_ascii=False)
