import json


# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = 'AIzaSyDK25Zi9td3dOqUbsUM8kfEOkJPfDutEtk'

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = self.channel_id
        channel =youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)