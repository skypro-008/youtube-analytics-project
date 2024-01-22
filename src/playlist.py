import os
import datetime
import isodate
from googleapiclient.discovery import build


class PlayList:

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)


    def __init__(self, playlist_id):
        self.playlist_videos = (PlayList.youtube.playlistItems().list
                                (playlistId=playlist_id, part='contentDetails,snippet', maxResults=50, ).execute())
        self.playlist_video = PlayList.youtube.playlists().list(id=playlist_id, part='snippet',
                                                                 maxResults=50, ).execute()

        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = PlayList.youtube.videos().list(part='contentDetails,statistics',
                                                        id=','.join(self.video_ids)).execute()
        self.playlist_id = playlist_id
        self.title = self.playlist_video['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"


    def __str__(self):
        return f'{self.title}, {self.url}'

    @property
    def total_duration(self):
        response = datetime.timedelta()

        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            response += duration
        return response

    def show_best_video(self):
        global best_video
        likes = 0
        for video_id in self.video_ids:
            video_request = self.youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()
            like_count = video_request['items'][0]['statistics']['likeCount']
            if int(like_count) > likes:
                likes = int(like_count)
                best_video = f"https://youtu.be/{video_request['items'][0]['id']}"
        return best_video

