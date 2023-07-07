import json
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

class Channel:
    """
    Класс для YouTube-канала
    """

    api_key: str = os.getenv('YT_API_KEY')

    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriberCount = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.viewCount = self.channel["items"][0]["statistics"]["viewCount"]

    def __str__(self):
        """
        Возвращает название канала и ссылку на него.
        """
        return f"{self.title} ({self.url})"


    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        print(self.channel)

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        # Метод для работы с YouTube API
        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, file_name):
        # Сохранение значений атрибутов в файл
        channel_data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.subscriberCount,
            "video_count": self.video_count,
            "viewCount": self.viewCount
        }
        with open(file_name, "w") as json_file:
            json.dump(channel_data, json_file)

    def __add__(self, other):
        """
        Возвращает сумму подписчиков 2 каналов.
        """
        total_subscribers = int(self.subscriberCount) + int(other.subscriberCount)
        return total_subscribers

    def __sub__(self, other):
        """
        возвращает разницу подписчиков 2 каналов
        """
        diff_subscribers = int(self.subscriberCount) - int(other.subscriberCount)
        return diff_subscribers


    def __gt__(self, other):
        """
        Возвращает True, если количество подписчиков текущего канала больше,
        чем у другого канала, и False в противном случае.
        """
        return int(self.subscriberCount) > int(other.subscriberCount)

    def __ge__(self, other):
        """
        Возвращает True, если количество подписчиков текущего канала больше или равно,
        другому каналу, и False в противном случае.
        """
        return int(self.subscriberCount) >= int(other.subscriberCount)

    def __lt__(self, other):
        """
        Возвращает True, если количество подписчиков текущего канала меньше,
        чем у другого канала, и False в противном случае.
        """
        return int(self.subscriberCount) < int(other.subscriberCount)

    def __le__(self, other):
        """
        Возвращает True, если количество подписчиков текущего канала меньше или равно,
        другому каналу, и False в противном случае.
        """
        return int(self.subscriberCount) <= int(other.subscriberCount)

    def __eq__(self, other):
        """
        Возвращает True, если количество подписчиков двух каналов равно, и False в противном случае.
        """
        return int(self.subscriberCount) == int(other.subscriberCount)

