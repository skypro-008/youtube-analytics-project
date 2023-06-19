import json
import os

from googleapiclient.discovery import build
class Video:
    API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    def __init__(self, video_id):
        self.video_id = video_id
        self.channel = self.youtube.videos().list(id=self.video_id, part='snippet,statistics,contentDetails,topicDetails').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]

        self.url = "https://www.youtube.com/watch?v=" + self.video_id

        self.likeCount = self.channel["items"][0]["statistics"]["likeCount"]
        self.viewCount = self.channel["items"][0]["statistics"]["viewCount"]

    def __str__(self):
        return self.title

class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title


