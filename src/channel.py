import json
import os

from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = "UC-OVMPlMA3-YCIeg4z5z23A"
        self.title = "MoscowPython"
        self.desription = "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
        self.url = "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"
        self.video_count = 685
        self.viewCount = 2303120
        self.subscriberCount = 25900

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        #channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # HighLoad Channel
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self):
        with open('data_json', "w", encoding='utf-8') as file:
            json.dump(data, file)