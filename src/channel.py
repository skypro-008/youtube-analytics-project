import os
import json
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.response = youtube.channels().list(
            part='snippet,contentDetails,statistics',
            id=channel_id
        ).execute()

        # Обработка полученного результата
        # self.channel = self.response['items'][0]
        # self.snippet = self.channel['snippet']
        # self.statistics = self.channel['statistics']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # Вывод результатов
        print(json.dumps(self.response, indent=2, ensure_ascii=False))