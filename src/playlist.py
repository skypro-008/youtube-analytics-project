import isodate, datetime
import json
import os
from pprint import pprint
from src.video import Video, PLVideo
from src.channel import Channel
from googleapiclient.discovery import build


class PlayList(PLVideo):
    api_key: str = os.getenv('API_KEY_YOUTUBE')

    def __init__(self, id_playlist):
        # super().__init__(id_playlist)
        self.id_playlist = id_playlist
        """GET запрос по id видео с необходимыми параметрами о плэйлисте. Возвращает данные о плайлиста в формате JSON """
        playlist_data = Video.get_service().playlistItems().list(playlistId=self.id_playlist,
                                                                 part='contentDetails,id,snippet',
                                                                 maxResults=50).execute()
        self.title_playlist = playlist_data['items'][0]['snippet']['title'].split('.')[0]
        self.url_playlist = "https://www.youtube.com/playlist?list=" + self.id_playlist

    def videos_id(self):
        """метод для получения списка id по данным плайлиста """
        playlist_videos = self.get_service().playlistItems().list(playlistId=self.id_playlist, part='contentDetails',
                                                                  maxResults=50).execute()
        playlist_videos_id: list[str] = [video['contentDetails']["videoId"] for video in playlist_videos['items']]
        return playlist_videos_id

    @property
    def total_duration(self):
        """метод для вывода суммарной длительности плейлиста"""
        time_total = datetime.timedelta(seconds=0)
        for item_id in PlayList.videos_id(self):
            video = Video(item_id)
            time_video = isodate.parse_duration(video.duration_video)
            time_total += time_video
        return time_total

    def show_best_video(self):
        """метод для вывода ссылку на самое популярное видео из плейлиста по лайкам"""
        best_likes_count_video = 0
        url_best_video = ""
        for item_id in PlayList.videos_id(self):
            video = Video(item_id)
            likes_video = int(video.likes_count_video)
            if likes_video > best_likes_count_video:
                best_likes_count_video = likes_video
                url_best_video = f"https://youtu.be/" + item_id

        return url_best_video
