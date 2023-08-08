import datetime
import isodate
import os
from googleapiclient.discovery import build


class PlayList:
    """
    Представляет плейлист YouTube и предоставляет методы для получения информации о плейлисте.
    """
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_playlist) -> None:
        """
        Инициализирует объект PlayList с заданным id_playlist
        """
        self.id_playlist = id_playlist

        playlists = self.youtube.playlists().list(
            part='snippet',
            id=self.id_playlist
        ).execute()

        self.title = playlists['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={id_playlist}'

    def video_details(self):
        """
        Получает детали видео для видео в плейлисте.
        """
        playlist_videos = self.youtube.playlistItems().list(
            playlistId=self.id_playlist,
            part='contentDetails',
            maxResults=50,
        ).execute()
        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = self.youtube.videos().list(
            part='contentDetails',
            id=','.join(video_ids)
        ).execute()
        return video_response['items']

    @property
    def total_duration(self):
        """
         Вычисляет общую продолжительность всех видео в плейлисте.
        """
        details = self.video_details()
        summ = []
        for video in details:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            summ.append(duration)
        total_duration = sum(summ, datetime.timedelta())
        return total_duration

    def show_best_video(self):
        """
        Находит и возвращает URL видео с наибольшим количеством лайков в плейлисте
        """
        max_like = 0
        best_id = None
        for video in self.video_details():
            id_video = video["id"]
            video_response = self.youtube.videos().list(
                part='statistics',
                id=id_video
            ).execute()
            like = int(video_response['items'][0]['statistics']['likeCount'])
            if like > max_like:
                max_like = like
                best_id = id_video
        best_video_url = f"https://youtu.be/{best_id}"
        return best_video_url
