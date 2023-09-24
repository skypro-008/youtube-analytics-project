import json
import os


from googleapiclient.discovery import build

api_key = os.getenv('API_YT')
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""
    __API_KEY: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url_chanel = f"https://www.youtube.com/{channel['items'][0]['snippet']['customUrl']}"
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls) -> build:
        """Возвращает объект для работы с API youtube."""
        service = build('youtube', 'v3', developerKey=cls.__API_KEY)
        return service

    def to_json(self, filename):
        info_chanel = {"title": self.title,
                       "description": self.description,
                       "url_chanel": self.url_chanel,
                       "subscriber_count": self.subscriber_count,
                       "video_count": self.video_count,
                       "view_count": self.view_count}
        with open(filename, "w", encoding="UTF-8") as file:
            json.dump(info_chanel, file, indent=2)


