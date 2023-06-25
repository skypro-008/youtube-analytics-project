import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')


class Channel:
    all = []
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.all.append(self)
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        for i in channel['items']:
            self.__channel_id = i["id"]
            self.title = i["snippet"]["title"]
            self.description = i["snippet"]["description"]
            self.url = f"https://www.youtube.com/channel/{i['id']}"
            self.subscriber_count = i["statistics"]['subscriberCount']
            self.video_count = i["statistics"]["videoCount"]
            self.view_count = i["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    def to_json(self, name) -> None:
        test_j = []
        test_j.append(getattr(self, "channel_id"))
        test_j.append(getattr(self, "title"))
        test_j.append(getattr(self, "url"))
        test_j.append(getattr(self, "description"))
        test_j.append(getattr(self, "subscriber_count"))
        test_j.append(getattr(self, "video_count"))
        test_j.append(getattr(self, "view_count"))
        with open(name, "w") as write_file:
            json.dump(test_j, write_file)

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
