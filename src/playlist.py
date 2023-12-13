import os
import datetime
import dotenv
import isodate
from googleapiclient.discovery import build

dotenv.load_dotenv()

youtube = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))


class PlayList:
    def __init__(self, play_list_id):
        self.play_list_id = play_list_id
        self.youtube = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))
        self.playlist = youtube.playlists().list(part='snippet', id='PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw').execute()['items'][0]
        self.playlist_items = youtube.playlistItems().list(
            playlistId='PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw',
            part='contentDetails, snippet',
            maxResults=50,
        ).execute()
        self.title = self.playlist['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={play_list_id}"
        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist_items['items']]
        self.video_response = self.youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(self.video_ids)
        ).execute()

    @property
    def total_duration(self):
        """
        возвращает общую длинну плей листа
        """
        total_duration = datetime.timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += datetime.timedelta(seconds=duration.total_seconds())
        return total_duration

    def show_best_video(self):
        """
        выдает видео с самым большим количеством лайков из плейлиста
        """
        like = 0
        max_like = ""

        for i in self.video_response['items']:
            video_id = i['id']
            like_count = int(i['statistics']['likeCount'])
            if like_count > like:
                like = like_count
                max_like = video_id
        return f'https://youtu.be/{max_like}'
