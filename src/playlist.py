import os
from datetime import timedelta

import isodate
from googleapiclient.discovery import build


class PlayList:
    def __init__(self, playlist_id):
        youtube = self.get_service()
        self.__playlist_id = playlist_id
        self.__response = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.__videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails'). \
            execute()
        self.__video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__videos['items']]
        self.__videos_response = youtube.videos().list(part='contentDetails,statistics',
                                                       id=','.join(self.__video_ids)).execute()
        self.title = self.__response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'

    @property
    def total_duration(self):
        duration = timedelta(hours=0, minutes=0)
        for video in self.__videos_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)
        return duration

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def show_best_video(self):
        best_video = self.__videos_response['items'][0]
        for video in self.__videos_response['items']:
            if video['statistics']['likeCount'] > best_video['statistics']['likeCount']:
                best_video = video
        return f'https://youtu.be/{best_video["id"]}'
