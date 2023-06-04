import os
import isodate
from datetime import timedelta
from googleapiclient.discovery import build
import json

class PlayList:

    API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, playlist_id) -> None:
        self.playlist_id = playlist_id
        self.playlist = self.youtube.playlists().list(part='snippet', id=self.playlist_id).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(self.video_ids)
                                                    ).execute()
        self.video_response_info = json.dumps(self.video_response, indent=2)


    @property
    def total_duration(self):
        """
        Возвращает объект класса `datetime.timedelta` с суммарной длительность плейлиста
        """

        total_duration = timedelta(hours=0, minutes=0, seconds=0)

        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration


    def show_best_video(self):
        """
        Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        """
        max_like_count = 0
        max_video_id = 0
        for video in self.video_response['items']:
            like_count = video["statistics"]["likeCount"]
            video_id = video['id']
            if int(like_count) > int(max_like_count):
                max_like_count = like_count
                max_video_id = video_id
        return f'https://youtu.be/{max_video_id}'