import os
from datetime import timedelta

import isodate
from googleapiclient.discovery import build

from src.Video import Video


class PlayList:
    """Класс для плейлиста ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey='AIzaSyAZomY9PsOL0gNN8BbgrlbNo9z6BVbmR7s')

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id

    def get_playlist_info(self):
        """Получает информацию о плейлисте"""
        self.list_playlist: dict = self.youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        self.title = self.list_playlist.get('items', {})[0].get('snippet', {}).get('title')
        self.url = "https://www.youtube.com/playlist?list=" + self.playlist_id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()

    @property
    def total_duration(self):
        """Возвращает длительность всех видео для плейлиста"""
        self.get_playlist_info()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]

        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()
        result = timedelta()

        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            result += isodate.parse_duration(iso_8601_duration)
        return result

    def show_best_video(self) -> str:
        self.get_playlist_info()
        statistic_list = []
        for video in self.playlist_videos['items']:
            video_id = str(video['contentDetails']['videoId'])
            statistic_list.append([video_id, int(Video(video_id).like_count)])

        return "https://youtu.be/" + "".join([x[0] for x in statistic_list
                                              if x[1] == max([x[1] for x in statistic_list])])



