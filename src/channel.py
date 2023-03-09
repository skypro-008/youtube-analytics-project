from src.utils import print_inf


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        pass

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print_inf(self.channel_id)
        pass
