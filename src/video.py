import os

from googleapiclient.discovery import build


class Video:
    API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, video_id):
        self.video_id = video_id
        self.channel = self.youtube.videos().list(id=self.video_id,
                                                  part='snippet,statistics,contentDetails,topicDetails').execute()
        try:
            self.title = self.channel["items"][0]["snippet"]["title"]
            self.url = "https://www.youtube.com/watch?v=" + self.video_id
            self.like_count = self.channel["items"][0]["statistics"]["likeCount"]
            self.view_count = self.channel["items"][0]["statistics"]["viewCount"]
        except IndexError:
            self.title = None
            self.url = None
            self.like_count = None
            self.view_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
