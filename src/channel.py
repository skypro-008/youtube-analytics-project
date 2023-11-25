from googleapiclient.discovery import build
import json
import os
import dotenv

dotenv.load_dotenv()


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channal_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print((json.dumps(self.youtube.channels().list(id=self.channal_id, part='snippet,statistics').execute())))
