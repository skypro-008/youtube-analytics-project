import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.api_key = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.video_response = self.youtube.videos().list(
            part='snippet,statistics,contentDetails,topicDetails',
            id=self.video_id).execute()
        self.video_title = self.video_response['items'][0]['snippet']['title']
        self.video_url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.view_count = int(self.video_response['items'][0]['statistics']['viewCount'])
        self.like_count = int(self.video_response['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return self.video_title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self. playlist_videos = self.youtube.playlistItems().list(
            playlistId=self.playlist_id, part='contentDetails',
            maxResults=50,).execute()
