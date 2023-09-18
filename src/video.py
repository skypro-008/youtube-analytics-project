from src.baseclass import MixinBase


class Video(MixinBase):
    """Класс для видео с Youtube"""

    def __init__(self, video_id: str):
        """Экземпляр инициализируется по id видео. Дальше все данные будут подтягиваться по API."""
        try:
            self.__video_id = video_id
            self.video_response = (
                self.get_service().videos().list(id=self.__video_id, part='snippet,statistics')).execute()
            self.title: str = self.video_response['items'][0]['snippet']['title']
            self.url: str = f"https://youtu.be/{self.__video_id}"
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']

        except:
            self.__video_id = video_id
            self.title: str = None
            self.url: str = None
            self.view_count: int = None
            self.like_count: int = None


def __str__(self):
    """представление класса для пользователя"""
    return self.title


class PLVideo(Video):
    """Класс плейлист YOUTUBE"""

    def __init__(self, video_id: str, playlist_id: str):
        """инициализация из родительского класса и дополнительного атрибута playlist_id"""
        super().__init__(video_id)
        self.playlist_id = playlist_id