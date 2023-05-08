import datetime
import os

import isodate
from googleapiclient.discovery import build

from src.video import Video

api_key = os.getenv('API_KEY_YOU_TUBE')
youtube = build('youtube', 'v3', developerKey=api_key)


class PlayList(Video):
    def __init__(self, playlist_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.playlist_id = playlist_id
        self.playlist = self.youtube.playlists().list(part='snippet', id=playlist_id).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"

    def total_duration(self):
        """
        Возвращает объект класса `datetime.timedelta` с суммарной длительность плейлиста
        """
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        total_video_diration = datetime.timedelta(hours=0, minutes=0, seconds=0)

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)

            duration_split = str(duration).split(':')
            duration = datetime.timedelta(hours=int(duration_split[0]), minutes=int(duration_split[1]),
                                          seconds=int(duration_split[2]))
            total_video_diration += duration

        return total_video_diration

    def show_best_video(self):
        """
        Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        """
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()

        video_like_count = 0
        video_url = ''
        for video in video_response['items']:

            like_count = int(video['statistics']['likeCount'])

            if like_count > video_like_count:
                video_like_count = like_count
                video_url = f"https://youtu.be/{video['id']}"

        return video_url
