from src.constants import YOUTUBE
import isodate


class Video:
    """
    Класс для ютуб-видео
    """
    def __init__(self, video_id: str) -> None:
        """
        Инициализация класса по id видео.
        """
        self.video: dict = YOUTUBE.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                 id=video_id
                                                 ).execute()
        self.video_id: str = video_id
        self.title: str = self.video['items'][0]['snippet']['title']
        self.url: str = f'https://www.youtube.com/watch?v={video_id}'
        self.view_count: int = self.video['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video['items'][0]['statistics']['likeCount']
        self.duration = isodate.parse_duration(self.video['items'][0]['contentDetails']['duration'])

    def __str__(self) -> str:
        """
        Информация об объекте для пользователей
        """
        return f'{self.title}'


    def __gt__(self, other: 'Video') -> bool:
        """
        Возвращает результат сравнения видео по количеству лайков
        """
        return self.like_count > other.like_count


class PLVideo(Video):
    """
    Класс для плейлистов ютуб
    """
    def __init__(self, video_id: str, playlist_id: str) -> None:

        super().__init__(video_id)
        self.playlist_id: str = playlist_id
