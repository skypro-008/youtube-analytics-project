import os
from datetime import timedelta

from googleapiclient.discovery import build

from src.video import PLVideo


class PlayList:
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist_response = self.youtube.playlists().list(part='snippet', id=self.playlist_id).execute()
        self.title = self.playlist_response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        self.videos = self.get_videos()

    def get_videos(self):
        videos = []
        next_page_token = None
        while True:
            playlist_items = self.youtube.playlistItems().list(part='snippet', playlistId=self.playlist_id,
                                                               maxResults=50, pageToken=next_page_token).execute()
            for item in playlist_items['items']:
                video_id = item['snippet']['resourceId']['videoId']
                videos.append(PLVideo(video_id, self.playlist_id))
            next_page_token = playlist_items.get('nextPageToken')
            if not next_page_token:
                break
        return videos

    @property
    def total_duration(self):
        total_time = timedelta()
        for video in self.videos:
            duration = self.youtube.videos().list(part='contentDetails', id=video.id_video).execute()['items'][0][
                'contentDetails']['duration']
            minutes, seconds = map(int, duration[2:].replace('M', ' ').replace('S', '').split())
            duration = timedelta(minutes=minutes, seconds=seconds)
            total_time += duration
        return total_time

    def show_best_video(self):
        best_video_id = None
        max_likes = 0
        for video in self.videos:
            statistics = self.youtube.videos().list(part='statistics', id=video.id_video).execute()['items'][0][
                'statistics']
            likes = int(statistics['likeCount'])
            if likes > max_likes:
                max_likes = likes
                best_video_id = video.id_video
        return f'https://youtu.be/{best_video_id}'
