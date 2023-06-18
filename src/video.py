from pprint import pprint

from googleapiclient.discovery import build
from src.utils import find_value
from src.youtube_object import YoutubeObject

import os


class Video(YoutubeObject):

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
        try:
            self.title: str = video_response['items'][0]['snippet']['title']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        except IndexError:
            pass


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id
