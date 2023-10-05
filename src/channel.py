import json
import os
from googleapiclient.discovery import build
import isodate
from dotenv import load_dotenv


class Channel:
    """Класс для ютуб-канала"""
    youtube = None

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        if Channel.youtube is None:
            Channel.youtube = build('youtube', 'v3', developerKey=Channel.__api_key())
        self.channel = Channel.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        (self.title, self.video_count, self.url, self.description,
         self.subscriber, self.view_count) = self.__get_cnannel_info()

    @staticmethod
    def __api_key():
        '''
        Считать API_KEY из переменных окружения
        '''
        api_key = ''
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.split(current_dir)[0]
        filepath = os.path.join(root_dir, '.env')
        if os.path.exists(filepath):
            load_dotenv(filepath)
            api_key = os.getenv('API_KEY')
        return api_key

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def __get_cnannel_info(self):
        ''' Получить данные по каналу '''
        title = ''
        video_count = ''
        url = ''
        items = self.channel.get('items')
        for item in items:
            if item is not None:
                if item.get('id') == self.channel_id:
                    url = ''.join(['https://www.youtube.com/channel/', self.channel_id])
                    snippet = item.get('snippet')
                    if snippet is not None:
                        title = snippet.get('title')
                        description = snippet.get('description')
                    statistics = item.get('statistics')
                    if statistics is not None:
                        video_count = statistics.get('videoCount')
                        subscriber = statistics.get('subscriberCount')
                        view_count = statistics.get('viewCount')
                break
        return title, video_count, url, description, subscriber, view_count

    @classmethod
    def get_service(cls):
        ''' Вернуть объект сервис '''
        return cls.youtube

    def to_json(self, filename):
        ''' Сохранить в JSON файле '''
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.split(current_dir)[0]
        filepath = os.path.join(root_dir, 'homework-2', filename)
        with open(file=filepath, encoding="utf-8", mode='w') as file:
            json.dump(self.channel, file)
