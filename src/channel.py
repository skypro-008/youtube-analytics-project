import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    channel_id = os.getenv("YT_API_KEY")
    youtube = build("youtube", "v3", developerKey=channel_id)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = (
            self.youtube.channels()
            .list(id=self.channel_id, part="snippet,statistics")
            .execute()
        )

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel)
