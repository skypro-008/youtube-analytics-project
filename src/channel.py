import json
import os
from googleapiclient.discovery import build
import isodate
from dotenv import load_dotenv


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=Channel.__api_key())
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()


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
