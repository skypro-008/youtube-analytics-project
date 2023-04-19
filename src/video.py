import os
from googleapiclient.discovery import build


class Video:

    api_key: str = os.getenv("YT_API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=video_id).execute()
        self.title = self.video_response['items'][0]['snippet']['title']
        self.url_video = f"https://youtu.be/{self.video_id}"
        self.viewCount = self.video_response['items'][0]['statistics']['viewCount']
        self.likeCount = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f'{self.title}'
