import json
import os
from googleapiclient.discovery import build

import isodate


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        api_key: str = os.getenv('YT_API_KEY')
        special_controller_yt = build('youtube', 'v3',
                                      developerKey=api_key)  # создать специальный объект для работы с API
        self.channel_summary_info = special_controller_yt.channels().list(id=self.channel_id,
                                                                          part='snippet,statistics').execute()  # получить информацию о канале

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале в json-подобном удобном формате с отступами"""
        print(json.dumps(self.channel_summary_info, indent=2, ensure_ascii=False))
