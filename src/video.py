import os

from googleapiclient.discovery import build


class Video:
    __api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        self.video_response = Video.youtube.videos().list(
            part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.video_title = self.video_response['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.video_id}'
        self.view_count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response['items'][0]['statistics']['likeCount']
