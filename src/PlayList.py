import os
from datetime import timedelta
from typing import Any

import isodate
from googleapiclient.discovery import build

from src.video import Video


class PlayList:
    """ Класс для плейлиста """
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id: str) -> None:
        """Экземпляр инициализируется id плейлиста """
        self.__id = playlist_id
        self.playlist = self.get_service().playlists().list(id=self.__id, part='snippet', maxResults=50).execute()
        self.title = self.playlist.get('items')[0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list=/{self.__id}'
        self.info_videos = self.get_service().playlistItems().list(playlistId=self.__id,
                                                                   part='contentDetails, snippet',
                                                                   maxResults=50).execute()
        self.video_ids = [video['contentDetails']['videoId'] for video in self.info_videos['items']]
        self.videos = [Video(video_id) for video_id in self.video_ids]

    def __str__(self) -> str:
        """ Возвращающает ссылку на плейлист """
        return f'{self.url}'

    @property
    def total_duration(self) -> Any:
        """ Возвращает объект класса с суммарной длительность плейлиста"""
        playlist_duration = timedelta(seconds=0)
        for video in self.videos:
            playlist_duration += isodate.parse_duration(video.duration)
        return playlist_duration

    def show_best_video(self) -> str:
        """ Возвращает ссылку на самое популярное видео из плейлиста"""
        best_video = max(self.videos, key=lambda i: i.likes_count)
        return best_video.url

    @classmethod
    def get_service(cls):
        return cls.youtube
