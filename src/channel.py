import os

from googleapiclient.discovery import build

# os.environ['YT_API_KEY'] = 'AIzaSyBpNdpo_fHPACm0Nopoj45bkRVeAjCpQcc'


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""


    def print_info(self) -> None:
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlists = youtube.playlists().list(channelId=self.channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        """Выводит в консоль информацию о канале."""

        print(playlists)
