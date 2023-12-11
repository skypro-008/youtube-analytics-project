import os
import datetime
import isodate

from googleapiclient.discovery import build
from src.video import Video


class PlayList:
    """
    Класс по плейлисту из ютуба
    """

    def __init__(self, id_playlist: str):
        self.id_playlist = id_playlist
        self.title = self.get_title_playlist()
        self.url = f"https://www.youtube.com/playlist?list={self.id_playlist}"

    def get_video_id(self):
        """
        Вовращает список видео по id из плейлиста
        """
        playlist_videos = (
            self.get_service()
            .playlistItems()
            .list(playlistId=self.id_playlist, part="contentDetails")
            .execute()
        )
        return [video["contentDetails"]["videoId"] for video in playlist_videos["items"]]

    def get_title_playlist(self):
        """Возвращает title плэйлиста для инициализации"""
        pl_info = (
            self.get_service()
            .playlists()
            .list(id=self.id_playlist, part="snippet")
            .execute()
        )
        title = pl_info["items"][0]["snippet"]["title"]
        return title

    @classmethod
    def get_service(cls) -> build:
        """
        Класс-метод, возвращающий объект для работы с YouTube API
        """
        channel_id = os.getenv("YT_API_KEY")
        cls.youtube = build("youtube", "v3", developerKey=channel_id)
        return build("youtube", "v3", developerKey=channel_id)

    @property
    def total_duration(self):
        """
        Возвращает объект класса с суммарной длительность плейлиста
        """
        video_response = (
            self.get_service()
            .videos()
            .list(part="contentDetails,statistics", id=",".join(self.get_video_id()))
            .execute()
        )
        total_duration_list = []
        for video in video_response["items"]:
            duration = video["contentDetails"]["duration"]
            all_duration = isodate.parse_duration(duration)
            total_duration_list.append(all_duration)
        td_ = datetime.timedelta(
            seconds=sum(td.total_seconds() for td in total_duration_list)
        )
        return td_

    def show_best_video(self):
        """
        Возвращает ссылку на самое популярное видео из плейлиста
        """
        video_ids = self.get_video_id()
        list_with_video_info = []
        for video_id in video_ids:
            video_info_dict = {}
            video_obj = Video(video_id)  # инициализация через класс Video
            video_info_dict["likes"] = video_obj.like_count
            video_info_dict["url"] = video_obj.url
            list_with_video_info.append(video_info_dict)
        sorted_list = sorted(
            list_with_video_info, key=lambda x: x["likes"], reverse=True
        )
        return sorted_list[0]["url"]
