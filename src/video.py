import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.title = ''
        self.view_count = 0
        self.like_count = 0
        self.get_video_info(video_id)

    def __str__(self):
        return self.title

    def get_video_info(self, video_id):
        api_key = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)

        video_response = youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        ).execute()

        if 'items' in video_response:
            video_info = video_response['items'][0]
            self.title = video_info['snippet']['title']
            self.view_count = int(video_info['statistics']['viewCount'])
            self.like_count = int(video_info['statistics']['likeCount'])


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
