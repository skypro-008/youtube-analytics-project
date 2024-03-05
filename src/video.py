import os
from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        try:
            self.video_id = video_id
            self.video_response = self.youtube.videos().list(
                part='snippet,statistics,contentDetails,topicDetails',
                id=self.video_id).execute()
            self.title: str = \
                self.video_response['items'][0]['snippet']['title']
            self.video_url = f"https://www.youtube.com/{self.video_id}"
            self.view_count: int = \
                self.video_response['items'][0]['statistics'][
                    'viewCount']
            self.like_count: int = \
                self.video_response['items'][0]['statistics'][
                    'likeCount']
        except IndexError:
            self.video_id = video_id
            self.video_response = None
            self.title = None
            self.video_url = None
            self.view_count = None
            self.like_count = None

        def __str__(self):
            return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id