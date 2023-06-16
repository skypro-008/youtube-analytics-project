
from googleapiclient.discovery import build


class Video():
    api_key = "AIzaSyAA_DGWlyk07XTfwlz507KCFoh2Q8AeM5Y"


    def __init__(self, video_id:str) -> None:

        youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.video_id = video_id
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.url = f'http://youtu.be{self.video_id}'
        self.like_count = video_response['items'][0]['statistics']['likeCount']
        self.video_title = video_response['items'][0]['snippet']['title']
        self.view_count = video_response['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):

    def __init__(self, id:str, playlistID:str):
        super().__init__(id)
        self.playlist = playlistID

