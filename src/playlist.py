import os
from googleapiclient.discovery import build


class PlayList:
    def __init__(self, playlist_id):
        """Реализация класса получение информации по id канала"""
        self.playlist_id = playlist_id
        api_key: str = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        self.playlist_videos = playlist_videos


        def __str__(self):
            """реализация сетода str"""
            return self.playlist_videos
        @property
        def total_duration():
            """возвращает объект класса datetime.timedelta с суммарной длительность плейлиста (обращение как к свойству, использовать @property)"""
            pass

        def show_best_video():
            """
            возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
            """
            pass


