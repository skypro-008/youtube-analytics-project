import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id):
        youtube = self.get_service()
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id).execute()
        self.video_id = video_id
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/channel/" + video_id
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.likes_count: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
