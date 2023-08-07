import os

from googleapiclient.discovery import build


class Video:
    """Класс видео с ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey='AIzaSyAZomY9PsOL0gNN8BbgrlbNo9z6BVbmR7s')

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id

        try:
            self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=self.video_id
                                                             ).execute()
            self.title: str = self.video_response['items'][0]['snippet']['title']
        except IndexError:
            self.title: str = None
            self.view_count: int = None
            self.like_count: int = None
            self.url: str = None

        else:
            self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=self.video_id
                                                             ).execute()
            self.title: str = self.video_response['items'][0]['snippet']['title']
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
            self.url: str = 'https://youtu.be/' + video_id

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id