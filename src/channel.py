import json
import os

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber_count = channel ['items'][0]['statistics']["subscriberCount"]
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.viewCount = channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        info = json.dumps(channel, indent=2, ensure_ascii=False)
        print(info)

    def __str__(self):
        return f'{self.title}({self.irl})'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def __ge__(self,other):
        return self.subscriber_count >= other.subscriber_count

    @property
    def channel_id(self) -> str:
        return self.__channel_id

    def to_json(self, file_name):
        dict = {}
        dict['id'] = self.channel_id
        dict['title'] = self.title
        dict['description'] = self.description
        dict['url'] = self.url
        dict['subscriberCount'] = self.subscriber_count
        dict['video_count'] = self.video_count

        with open(file_name, 'w') as f:
            json.dump(dict, f, indent=2)

    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        object_get = build('youtube','v3', developerKey=api_key)
        return object_get
