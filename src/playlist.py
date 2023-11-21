import os
import isodate
from googleapiclient.discovery import build
from src.apimixin import APIMixin
import datetime
from src.video import Video




class PlayList(APIMixin):
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, id_play_list):
        self.id_play_list = id_play_list
        self.url = f'https://www.youtube.com/playlist?list={self.id_play_list}'
        self.playlists = PlayList.get_service().playlists().list(id=id_play_list,
                                                                 part='contentDetails,snippet',
                                                                 maxResults=50,
                                                                 ).execute()
        self.title = self.playlists['items'][0]['snippet']['title']


    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)


    def total_duration(self):
        time_list = []
        total_time = 0

        self.playlist_videos = PlayList.get_service().playlistItems().list(playlistId=self.id_play_list,
                                                                           part='contentDetails',
                                                                           maxResults=50,
                                                                           ).execute()

        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        video_response = PlayList.get_service().videos().list(part='contentDetails,statistics',
                                                              id=','.join(self.video_ids)
                                                              ).execute()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            time_list.append(str(duration))

        for time in time_list:
            date_time = datetime.datetime.strptime(time, '%H:%M:%S')
            a_timedelta = date_time - datetime.datetime(1900, 1, 1)
            seconds = a_timedelta.total_seconds()
            total_time += seconds

        time_duration = datetime.timedelta(seconds=total_time)

        return time_duration


    def show_best_video(self):
        self.playlist_videos = PlayList.get_service().playlistItems().list(playlistId=self.id_play_list,
                                                                           part='contentDetails',
                                                                           maxResults=50,
                                                                           ).execute()

        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        video_response = PlayList.get_service().videos().list(part='contentDetails,statistics',
                                                              id=','.join(self.video_ids)
                                                              ).execute()

        for video_id in self.video_ids:
            video = Video(video_id)
            max_views_video = '0'
            if video.view_count > max_views_video:
                best_video = video.url
                max_views_video = video.view_count

        return best_video
