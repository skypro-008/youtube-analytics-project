from googleapiclient.discovery import build
from src.utils import find_value

import os


class Video:
    service_name: str = 'youtube'
    service_version: str = 'v3'
    yt_api_key: str = os.getenv('YT_API_KEY')
    service = build(service_name, service_version, developerKey=yt_api_key)

    def __init__(self, video_id):
        self.__video_id = video_id
        self.video_url = 'https://www.youtube.com/watch?v=' + video_id

        self.title = None
        self.view_count = None
        self.like_count = None

        self.set_video_info()

    def __str__(self):
        return self.title

    def set_video_info(self):
        video_response = Video.service.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                     id=self.__video_id
                                                     ).execute()

        self.title: str = find_value(video_response, 'title')
        self.view_count: int = int(find_value(video_response, 'viewCount'))
        self.like_count: int = int(find_value(video_response, 'likeCount'))


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id
