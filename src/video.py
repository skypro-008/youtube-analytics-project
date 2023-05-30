from src.channel import Channel
from src.utils import find_value


class Video(Channel):
    """Класс для ютуб-видео"""

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется по id видео. Дальше все данные будут подтягиваться по API."""

        self._video_id = video_id
        self._title = None
        self._url = None
        self._views_count = None
        self._likes_count = None

        self.set_atr()

    @property
    def video_id(self) -> str:
        return self._video_id

    @video_id.setter
    def video_id(self, video_id: str):
        self._video_id = video_id
        self.set_atr()

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, url: str):
        self._url = url

    @property
    def views_count(self) -> str:
        return self._views_count

    @views_count.setter
    def views_count(self, views_count: str):
        self._views_count = views_count

    @property
    def likes_count(self) -> str:
        return self._likes_count

    @likes_count.setter
    def likes_count(self, likes_count: str):
        self._likes_count = likes_count

    def get_info(self) -> dict:
        """Получает данные о видео по его id"""

        manager = self.get_service()

        video_info = manager.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                           id=self.video_id
                                           ).execute()
        return video_info

    def set_atr(self) -> None:
        """
        Устанавливает значения основных атрибутов объекта
        на основании полученных по id данных видео
        """

        video_info = self.get_info()

        self.title = find_value(video_info, "title")
        self.url = f'https://www.youtube.com/watch?v={find_value(video_info, "id")}'
        self.views_count = find_value(video_info, "viewCount")
        self.likes_count = find_value(video_info, "likeCount")

    def __str__(self) -> str:
        """Возвращает строку в формате: `<название_видео>`"""

        return f"{self.title}"


class PLVideo(Video):
    """Класс для ютуб-видео, принимающий также id плейлиста"""

    def __init__(self, video_id: str, video_pl: str) -> None:
        super().__init__(video_id)
        self._video_pl = video_pl