import json
import os
from googleapiclient.discovery import build


class Channel:
    """
    Класс для ютуб-канала
    """

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.__channel_id = channel_id
        self.api_key = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.channel_description = self.channel["items"][0]["snippet"]["description"]
        # self.url = self.channel["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscribers_count = int(self.channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = int(self.channel["items"][0]["statistics"]["videoCount"])
        self.views_count = int(self.channel["items"][0]["statistics"]["viewCount"])

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.subscribers_count + other.subscribers_count

    def __sub__(self, other):
        return self.subscribers_count - other.subscribers_count

    def __eq__(self, other):
        return self.subscribers_count == other.subscribers_count

    def __lt__(self, other):
        return self.subscribers_count < other.subscribers_count

    def __le__(self, other):
        return self.subscribers_count <= other.subscribers_count

    def __gt__(self, other):
        return self.subscribers_count > other.subscribers_count

    def __ge__(self, other):
        return self.subscribers_count >= other.subscribers_count

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info_in_json_format = json.dumps(self.channel, indent=2, ensure_ascii=False)
        print(channel_info_in_json_format)

    @classmethod
    def get_service(cls):
        """
        Класс-метод,возвращающий объект для работы с YouTube API
        """
        api_key = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, file_name):
        """
        Метод сохраняет в файл значения атрибутов экземпляра класса Channel
        """
        atrbt_dic = {"channel_id": self.__channel_id,
                     "title": self.title,
                     "channel_description": self.channel_description,
                     "url": self.url,
                     "subscribers_count": self.subscribers_count,
                     "video_count": self.video_count,
                     "views_count": self.views_count
                     }
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(atrbt_dic, file)

####################################################################################
# test_class = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
# print(test_class.channel)
# channel = Channel.get_service().channels().list(id=test_class.chanel_id, part='snippet,statistics').execute()
# print(channel)
# test_class.to_json('moscowpython.json')
# with open('moscowpython.json', "r") as fp:
#     fp_data = json.load(fp)
# print(fp_data)
