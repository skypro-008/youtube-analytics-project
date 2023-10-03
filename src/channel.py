import json
import os
from googleapiclient.discovery import build
import isodate
from dotenv import load_dotenv
import pprint


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key = self._load_api()


    def _load_api(self):
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
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))