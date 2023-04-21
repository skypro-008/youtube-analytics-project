import os
import datetime

from googleapiclient.discovery import build
import isodate


class PlayList():
    def __init__(self, playlist_id):
        """Реализация класса получение информации по id канала"""
        self.playlist_id = playlist_id
        api_key: str = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.playlist_data = self.youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        self.title = self.playlist_data['items'][0]['snippet']['title']
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in
                                     self.playlist_videos['items']]  # список ID видео
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',  # словарь видео
                                                         id=','.join(self.video_ids)
                                                         ).execute()

    def __str__(self):
        """реализация сетода str"""
        return f'{self.playlist_videos}'

    @property
    def total_duration(self):
        """Подсчет общей длительности плейлиста"""
        total_duration = datetime.timedelta()  # обьявление экземпляра класса timedelta() модуля datetime
        for video in self.video_response['items']:
            duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео в плейлисте"""
        sorted_videos = sorted(self.video_response['items'], key=lambda x: int(x['statistics']['viewCount']),
                               reverse=True) # сортируем
        best_video_id = sorted_videos[0]['id'] # берем первый элемент
        return f"https://youtu.be/{best_video_id}"
