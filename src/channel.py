from googleapiclient.discovery import build
import json
import os


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = self.__channel["items"][0]["id"]
        self.__title = self.__channel["items"][0]["snippet"]["title"]
        self.__video_count = int(self.__channel["items"][0]["statistics"]["videoCount"])
        self.__url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.__description = self.__channel["items"][0]["snippet"]["description"]
        self.__view_count = int(self.__channel["items"][0]["statistics"]["viewCount"])
        self.__subscriber_count = int(self.__channel["items"][0]["statistics"]["subscriberCount"])

    @property
    def channel(self):
        return self.__channel

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.__title

    @property
    def video_count(self):
        return self.__video_count

    @property
    def url(self):
        return self.__url

    @property
    def description(self):
        return self.__description

    @property
    def view_count(self):
        return self.__view_count

    @property
    def subscriber_count(self):
        return self.__subscriber_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, file_path: str = "channel.json"):
        with open(file_path, "w") as file:
            json.dump({"channel_id": self.__channel_id,
                       "title": self.__title,
                       "video_count": self.__video_count,
                       "url": self.__url,
                       "description": self.__description,
                       "view_count": self.__view_count,
                       "subscriber_count": self.__subscriber_count},
                      file)

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __radd__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count
