import json
import os
from googleapiclient.discovery import build

import isodate


class Channel:
    """Класс для ютуб-канала"""

    @classmethod
    def get_service(cls):
        """Возвращает специальный объект для работы с ютуб-API"""
        return build('youtube', 'v3', developerKey=os.environ['YT_API_KEY'])

    def __init__(self, channel_id: str):
        """При инициализации создаются атрибуты с основной информацией о канале"""
        self.channel_id = channel_id
        self.channel_summary_info = self.get_service().channels().list(id=self.channel_id,
                                                                       part='snippet,statistics').execute()  # получить информацию о канале

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале в json-подобном удобном формате с отступами"""
        print(json.dumps(self.channel_summary_info, indent=2, ensure_ascii=False))
