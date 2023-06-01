import os
from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails',
                                                    id=self.video_id).execute()

        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'{self.video_id}' \
               f'{self.video_title}' \
               f'{self.like_count}' \
               f'{self.comment_count}'

    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'{self.playlist_id}' \
               f'{self.video_id}' \
               f'{self.video_title}' \
               f'{self.view_count}' \
               f'{self.like_count}' \
               f'{self.comment_count}'

    def __str__(self):
        return super().__str__()
