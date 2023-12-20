import os
import json
from googleapiclient.discovery import build



def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

class Channel:
    """
    Класс для ютуб-канала
    """

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. 
        Дальше все данные будут подтягиваться по API.
        """
        self.channel_id = channel_id
        
        channel_info = self.get_service().channels().list(id=self.channel_id, 
                                                   part='snippet,statistics').execute()

        self.title = channel_info['items'][0]['snippet']['title']
        self.channel_desc = channel_info['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.count_sub = channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = channel_info['items'][0]['statistics']['videoCount']
        self.view_count = channel_info['items'][0]['statistics']['viewCount']
    
    @classmethod
    def get_service(cls):
        """
        Класс-метод
        :return: объект для работы с YouTube API
        """
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube

    def to_json(self, name_file):
        with open(f"src/{name_file}", 'w') as file:
            json.dump(self.__dict__, file)

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        channel = self.get_service().channels().list(id=self.channel_id, 
                                                   part='snippet,statistics').execute()
        printj(channel)
