import json
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    load_dotenv()

    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = (
            self.youtube.channels()
            .list(id=channel_id, part="snippet,statistics")
            .execute()
        )

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
