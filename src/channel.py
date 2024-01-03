from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        api_key = 'AIzaSyCWMbqApjkYh1yy_Bk9kiAbUjv1fI9EH0E'
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.channels().list(part='snippet, statistics', id=self.channel_id)
        response = request.execute()

        print(response)
