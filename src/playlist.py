import os
from datetime import timedelta
from googleapiclient.discovery import build


class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.api_key = os.environ.get('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.title, self.url = self.get_playlist_info()

    @property
    def total_duration(self):
        playlist_items = self.youtube.playlistItems().list(
            part='contentDetails',
            playlistId=self.playlist_id
        ).execute()

        total_duration = timedelta()
        for item in playlist_items['items']:
            video_id = item['contentDetails']['videoId']
            video_info = self.youtube.videos().list(
                part='contentDetails',
                id=video_id
            ).execute()
            duration = video_info['items'][0]['contentDetails']['duration']
            converted_duration = self.convert_duration(duration)
            print(f"Video: {video_id}, Duration: {converted_duration}")
            total_duration += converted_duration

        return total_duration

    def show_best_video(self):
        playlist_items = self.youtube.playlistItems().list(
            part='snippet',
            playlistId=self.playlist_id
        ).execute()

        best_video = None
        max_views = 0

        for item in playlist_items['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_info = self.youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()

            if 'viewCount' in video_info['items'][0]['statistics']:
                view_count = video_info['items'][0]['statistics']['viewCount']
                print(f"Video ID: {video_id}, Views: {view_count}")

                if int(view_count) > max_views:
                    max_views = int(view_count)
                    best_video = f"https://youtu.be/{video_id}"

        return best_video

    def get_playlist_info(self):
        playlist_info = self.youtube.playlists().list(
            part='snippet',
            id=self.playlist_id
        ).execute()

        title = playlist_info['items'][0]['snippet']['title']
        url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        return title, url

    @staticmethod
    def convert_duration(duration):
        if not duration:
            return timedelta()

        duration = duration.replace('PT', '').replace('H', ':').replace('M', ':').replace('S', '')
        elements = duration.split(':')
        hours, minutes, seconds = 0, 0, 0

        if len(elements) == 3:
            hours = int(elements[0]) if elements[0] else 0
            minutes = int(elements[1]) if elements[1] else 0
            seconds = int(elements[2]) if elements[2] else 0
        elif len(elements) == 2:
            minutes = int(elements[0]) if elements[0] else 0
            seconds = int(elements[1]) if elements[1] else 0

        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
