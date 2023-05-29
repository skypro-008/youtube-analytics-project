import os
import isodate
from datetime import timedelta
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()


class PlayList:
    yt_api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=yt_api_key)

    def __init__(self, playlist_id: str) -> None:
        self.playlist_id = playlist_id
        self.title = self.__update_title()
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        self.__total_duration = self.__update_total_duration()

    def __str__(self):
        return self.__total_duration

    def __get_data_playlist(self):
        return self.youtube.playlists().list(id=self.playlist_id, part='snippet').execute()

    def __get_playlist_videos(self):
        return self.youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails,snippet').execute()

    def __get_data_videos(self):
        return self.youtube.videos().list(part='contentDetails,statistics',
                                          id=','.join(self.__get_video_ids())).execute()

    def __update_title(self):
        data = self.__get_data_playlist()
        return data.get('items')[0].get('snippet').get('title')

    def __get_video_ids(self):
        data = self.__get_playlist_videos()
        return [video.get('contentDetails').get('videoId') for video in data.get('items')]

    def __update_total_duration(self):
        videos = self.__get_data_videos()
        total_duration = timedelta()
        for video in videos.get('items'):
            iso_8601_duration = video.get('contentDetails').get('duration')
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    @property
    def total_duration(self):
        return self.__total_duration

    def show_best_video(self):
        videos = self.__get_data_videos()

        likes_count = 0
        cur_video_id = ''

        for item in videos.get('items'):
            if likes_count < int(item.get('statistics').get('likeCount')):
                likes_count = int(item.get('statistics').get('likeCount'))
                cur_video_id = item.get('id')
        return f"https://youtu.be/{cur_video_id}"
