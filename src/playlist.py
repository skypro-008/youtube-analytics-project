from src.constants import YOUTUBE
from datetime import timedelta
from src.video import Video


class PlayList:
    """
    Класс для плейлиста
    """
    def __init__(self, playlist_id: str) -> None:
        """
        Инициализация класса по id плейлиста.

        """
        self.playlist_id: str = playlist_id
        self.playlist: dict = YOUTUBE.playlists().list(id=playlist_id,
                                                       part='snippet',
                                                       ).execute()
        self.playlist_videos: dict = YOUTUBE.playlistItems().list(playlistId=playlist_id,
                                                                  part='contentDetails'
                                                                  ).execute()
        self.title: str = self.playlist['items'][0]['snippet']['title']
        self.url: str = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        self.videos: list = [Video(video['contentDetails']['videoId'])
                             for video in self.playlist_videos['items']]


    @property
    def total_duration(self) -> timedelta:
        """
        Возвращает суммарную длительность видео плейлиста
        """
        total_duration = timedelta(0)
        for video in self.videos:
            total_duration += video.duration
        return total_duration


    def show_best_video(self) -> str:
        """
        Возвращает ссылку на видео с наибольшим количеством лайков
        """
        best_video = self.videos[0]
        for video in self.videos:
            if video > best_video:
                best_video = video
        return best_video.url
