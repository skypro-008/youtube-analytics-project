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
        print(api_key)
        print(youtube)

        channel_id = 'UCYp3rk70ACGXQ4gFAiMr1SQ'  # HighLoad Channel
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)
        intr = json.load(channel)
        intr = channel["items"]
        print(intr)
        intro = intr["kind"]
        print(type(intro))
        print(intro)

