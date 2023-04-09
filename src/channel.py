import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def __str__(self):
        return f"{self.channel_id}"

    def print_info(self, dict_to_print: dict) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
