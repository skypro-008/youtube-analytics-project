import os
from googleapiclient.discovery import build
import isodate
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.base_url = 'https://www.googleapis.com/youtube/v3/channels'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.environ.get("API_YUTUBE_KEY")
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)

        channel_id = self.channel_id  # HighLoad Channel
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)

        intro = channel["items"][0]
        print(f'\nНазвание канала - {intro["snippet"]["title"]}')
        print(f'Описание канала - {intro["snippet"]["description"]}')
        print(f'Дата публикации канала - {intro["snippet"]["publishedAt"][:10]}')
        print(f'Количество просмотров - {intro["statistics"]["viewCount"]}  человек')
        print(f'Количество подписок - {intro["statistics"]["subscriberCount"]}  человек')
        print(f'Количество роликов на канале - {intro["statistics"]["videoCount"]}  человек')



