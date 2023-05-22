import os
from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('YouTube_API_key')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                 id=video_id
                                                 ).execute()
        try:
            self.video['items'][0]
        except IndexError:
            print('Non_existent_video_error: Данного видео не существует!')
            self.title = None
            self.id = None
            self.name = None
            self.url = None
            self.view_count = None
            self.like_count = None
        else:
            self.id = self.video['items'][0]['id']
            self.name = self.video['items'][0]['snippet']['title']
            self.url = 'https://www.youtube.com/watch?v=' + self.id
            self.view_count = self.video['items'][0]['statistics']['viewCount']
            self.like_count = self.video['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.name


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.pl_id = Video.youtube.playlistItems().list(playlistId=playlist_id,
                                                        part='contentDetails',
                                                        maxResults=50,
                                                        ).execute()
