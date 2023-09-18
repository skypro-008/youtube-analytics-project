import datetime
import os
from googleapiclient.discovery import build
import isodate

class PlayList:
    api_key = os.getenv('YT_API_KEY')
    """Класс для плейлиста"""
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        #информация по всем видео из плейлиста
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                               part='contentDetails,snippet',
                                               maxResults=50,
                                               ).execute()
        # список id всех видео из плейлиста
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=','.join(self.video_ids)
                                                         ).execute()
        self.channel_id = self.playlist_videos['items'][0]['snippet']['videoOwnerChannelId']
        self.playlists = self.youtube.playlists().list(channelId=self.channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        for playlist in self.playlists['items']:
            if playlist['id'] == self.playlist_id:
                self.title = playlist['snippet']['title']
                break

    @property
    def total_duration(self):
        delta = datetime.timedelta(seconds=0,
                                   minutes=0,
                                   hours=0)
        total_duration = delta
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration

    def show_best_video(self):
        best_video_id = ''
        like_count = 0
        for video in self.video_response['items']:
            self.like_count = int(video['statistics']['likeCount'])

            if self.like_count > like_count:
                like_count = self.like_count
                best_video_id = video['id']
        return f'https://youtu.be/{best_video_id}'

    @total_duration.setter
    def total_duration(self, value):
        self._total_duration = value
