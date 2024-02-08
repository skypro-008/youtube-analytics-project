import os
import isodate
import datetime
from googleapiclient.discovery import build


class PlayList:
    YT_APY_KEY = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=YT_APY_KEY)

    def __init__(self, id_playlist):
        self.id_playlist = id_playlist
        playlist_info = self.youtube.playlists().list(id=id_playlist,
                                                      part='contentDetails,snippet',
                                                      ).execute()
        self.title = playlist_info['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={id_playlist}'
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=id_playlist,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                         id=','.join(self.video_ids)
                                                         ).execute()

    @property
    def total_duration(self):
        total_duration = datetime.timedelta(seconds=0)
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += datetime.timedelta(seconds=duration.total_seconds())
        return total_duration

    def show_best_video(self):
        max_like_count = 0
        best_video_url = ''
        for video_id in self.video_ids:
            video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=video_id
                                                        ).execute()
            if int(video_response['items'][0]['statistics']['likeCount']) > max_like_count:
                max_like_count = int(video_response['items'][0]['statistics']['likeCount'])
                best_video_url = f"https://youtu.be/{video_response['items'][0]['id']}"
        return best_video_url
