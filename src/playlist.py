from googleapiclient.discovery import build
from datetime import timedelta
# import os
import isodate


class PlayList:
    """
    Класс для работы с плейлистом канала YouTube.
    """
    def __init__(self, pl_id):
        """
        Конструктор класса PlayList.
        """
        self.pl_id: str = pl_id  # id play-листа
        playlist_videos = self._get_pl_info()
        video_response = self._get_video_info()
        self.title: str = playlist_videos['items'][0]['snippet']['title']  # название play-листа
        self.url: str = f'https://www.youtube.com/playlist?list={playlist_videos["items"][0]["id"]}'
        self.like_count_video: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        """
        Метод возвращающий суммарную длительность playlist.
        """
        return self.total_duration

    @classmethod
    def get_service(cls):
        """
        Класс-метод создает объект YouTube.
        """
        api_key: str = "AIzaSyBIE1Zoz-q-0QXM1H8hp3e_N9xnuT_9xfI"
        # api_key: str = os.getenv('YT_API_KEY')  # Получен токен
        youtube = build('youtube', 'v3', developerKey=api_key)  # Специальный объект для работы с API
        return youtube

    def _get_pl_info(self):
        """
        Метод возвращает информацию о плейлисте, полученную из объекта YouTube.
        """
        playlist_videos = self.get_service().playlists().list(
            id=self.pl_id, part='snippet', maxResults=50
        ).execute()
        return playlist_videos

    def _get_video_info(self):
        """
        Метод возвращает информацию о видео, полученную из объекта YouTube.
        """
        playlist_videos = self.get_service().playlistItems().list(playlistId=self.pl_id, part='contentDetails',
                                                                  maxResults=50, ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                          id=','.join(video_ids)).execute()
        return video_response

    @property
    def total_duration(self):
        """
        Метод для определения общего времени playlist.
        """
        total_duration = timedelta()
        video_response = self._get_video_info()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            time = str(duration).split(":")
            duration = timedelta(hours=int(time[0]), minutes=int(time[1]), seconds=int(time[2]))
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """
        Метод возвращающий ссылку на самое популярное видео.
        """
        video_response = self._get_video_info()
        sorted_like_count = sorted(video_response['items'], key=lambda x: int(x['statistics']['likeCount']),
                                   reverse=True)
        max_like_count_video_id = sorted_like_count[0]['id']
        return f"https://youtu.be/{max_like_count_video_id}"
