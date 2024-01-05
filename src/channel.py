from os import environ as env
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = env.get('YT_API_KEY') if env.get('YT_API_KEY') is not None else env.get('API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    # classmethods
    @classmethod
    def get_service(cls):
        """
        Создает объект Resource для работы с YouTube Dara API с помощью api_key.
        :return: Объект Resource
        """
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube

    # methods
    def channel_info(self) -> dict:
        """
        Получает информацию о канале через API, путем выполнения запроса к YT Data API.
        :return: Словарь с информацией о канале
        """
        request = Channel.get_service().channels().list(part='snippet, statistics', id=self.channel_id)
        response = request.execute()

        return response

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_info())
