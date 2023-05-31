import datetime
import json
import os
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource
from src.utils import find_value
from functools import total_ordering
from src.channel import Channel
import isodate


class PlayList(Channel):
    """Класс для описания плейлиста"""

    def __init__(self, playlist_id: str) -> None:
        """Экземпляр инициализируется по id плейлиста. Дальше все данные будут подтягиваться по API."""
        # noinspection PyMissingConstructor

        self.__playlist_id = playlist_id
        self.manager = self.get_service()
        self.title = None
        self.url = None

        self.set_atr()

        self.__total_duration = self.get_total_duration()

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def playlist_id(self) -> str:
        return self.__playlist_id

    @property
    def total_duration(self) -> datetime:
        return self.__total_duration

    def get_playlist_info(self) -> dict:
        """Возвращает данные о плейлисте по его id"""

        playlist_response = self.manager.playlists().list(part='snippet',
                                                          id=self.playlist_id
                                                          ).execute()

        return playlist_response

    def get_total_duration(self) -> datetime:
        """Возвращает общую длительность всех видеороликов плейлиста"""

        videos_info = self.get_videos_info()
        list_durations = list(map(self.to_timedata, videos_info["items"]))
        total_duration = sum(list_durations, datetime.timedelta())
        return total_duration

    @staticmethod
    def to_timedata(video: dict) -> datetime:
        """Возвращает длительность видеоролика в формате datetime"""

        video_duration = video['contentDetails']['duration']
        duration = isodate.parse_duration(video_duration)
        return duration

    def get_videos_info(self) -> dict:
        """Возвращает информацию о видеороликах плейлиста в формате словаря"""

        playlist_videos = self.manager.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        videos_info = self.manager.videos().list(part='contentDetails,statistics',
                                                 id=','.join(video_ids)
                                                 ).execute()

        return videos_info

    def show_best_video(self) -> str:
        """Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""

        videos_info = self.get_videos_info()

        likes = lambda video: video["statistics"]["likeCount"]
        url = lambda video: video["id"]

        popularity = {likes(video): url(video) for video in videos_info["items"]}
        best_video = popularity[max(popularity.keys())]

        return f"https://youtu.be/{best_video}"

    def set_atr(self) -> None:
        """
        Устанавливает значения основных атрибутов объекта
        на основании полученных по id данных плейлиста
        """

        playlist_videos = self.get_playlist_info()

        self.title = find_value(playlist_videos, "title")
        self.url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'
