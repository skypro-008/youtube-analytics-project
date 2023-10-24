import os
from googleapiclient.discovery import build


class Video:

    def __init__(self, video_id):
        self.__api_key = os.getenv('API_KEY')
        self.__youtube = build('youtube', 'v3', developerKey=self.__api_key)
        self.video_id = video_id
        self.video_response = self.__youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                           id=self.video_id
                                                           ).execute()
        self.video_title = self.video_response['items'][0]['snippet']['title']
        self.view_count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response['items'][0]['statistics']['likeCount']
        self.comment_count = self.video_response['items'][0]['statistics']['commentCount']

    def __str__(self):
        return self.video_title

    def __repr__(self):
        return self.video_response


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

