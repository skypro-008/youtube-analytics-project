from helper.youtube_api_manual import youtube


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics', maxResults=50).execute()
        print(channel)
