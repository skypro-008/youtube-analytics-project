import datetime
import os

import isodate
from googleapiclient.discovery import build


class PlayList:
    api_key: str = os.getenv('YouTube_API_key')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.url = "https://www.youtube.com/playlist?list=" + playlist_id
        self.playlist_videos = PlayList.youtube.playlistItems().list(playlistId=playlist_id,
                                                                     part='contentDetails',
                                                                     maxResults=50,
                                                                     ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]

    @property
    def total_duration(self):
        video_response = PlayList.youtube.videos().list(part='contentDetails,statistics',
                                                        id=','.join(self.video_ids)
                                                        ).execute()
        total_time = datetime.timedelta(0)
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_time += duration
        return total_time

    def show_best_video(self):
        best_like_count = 0
        best_video_url = ""
        for video in self.video_ids:
            video_response = PlayList.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video
                                                   ).execute()
            like_count: int = video_response['items'][0]['statistics']['likeCount']
            if int(like_count) > best_like_count:
                best_video_url = "https://youtu.be/" + video_response['items'][0]['id']
        return best_video_url
