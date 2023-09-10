from src.channel import Channel


class Video(Channel):
    """
    Класс для видео с ютуб-канала.
    Наследуется от класса ютуб-канала, чтобы не дублировать атрибуты и методы получения данных по API с ютуба.
    """

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.id_video = video_id
        self.video_response = self.get_service().videos().list(part='snippet,'
                                                                    'statistics,'
                                                                    'contentDetails,'
                                                                    'topicDetails',
                                                               id=video_id
                                                               ).execute()
        self.title: str = self.video_response['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/watch?v={video_id}"
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        """Строковое представление экземпляра класса"""
        return self.title


class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id: str) -> None:
        """Экземпляр инициализируется 'id видео' из родительского класса и 'id плейлиста'"""
        super().__init__(video_id)
        self.playlist_id = playlist_id