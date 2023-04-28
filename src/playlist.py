import datetime
import os
from googleapiclient.discovery import build
import isodate


class PlayList:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id: str) -> None:
        self.video_url = None
        self.playlist_id = playlist_id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                                 part='snippet, contentDetails, id, status',
                                                                 maxResults=50).execute()
        self.channel_id = self.playlist_videos['items'][0]['snippet']['channelId']
        self.playlists = self.youtube.playlists().list(part='snippet', channelId=self.channel_id,
                                                       maxResults=50).execute()

        for item in self.playlists['items']:
            if item['id'] == self.playlist_id:
                self.title = item['snippet']['title']
                break

        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails',
                                                         id=','.join(self.video_ids)
                                                         ).execute()
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

    @property
    def total_duration(self):
        total_time_videos = datetime.timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_time_videos += duration
        return total_time_videos

    def show_best_video(self):
        like_count = 0
        for video in self.video_response['items']:
            video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=video['id']).execute()
            if int(video_response['items'][0]['statistics']['likeCount']) > like_count:
                like_count = int(video_response['items'][0]['statistics']['likeCount'])
                self.video_url = video_response['items'][0]['id']

        return f'https://youtu.be/{self.video_url}'

    def __repr__(self):
        return f'{self.playlist_videos}'
