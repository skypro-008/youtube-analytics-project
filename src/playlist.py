import datetime
import json
import os
from functools import reduce
import operator

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)
class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        self.playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails,snippet',
                                                       maxResults=50,
                                                       ).execute()
        self.title = self.playlist_videos["items"][-2]["snippet"]["title"]
        print(self.title)
    def __str__(self):
        return f"{self.title} {self.url}"
    @property
    def total_duration(self):
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        duration_sum = []
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            duration_sum.append(duration)
            q = sum(duration_sum, datetime.timedelta())
        return q
    def show_best_video(self):
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        best_video = 0
        for video in video_response['items']:
            video_int = int(video["statistics"]["likeCount"])
            if video_int > best_video:
                best_video = video_int
        print(best_video)
        return f"https://youtu.be/{video['id']}"

