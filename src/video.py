import os
from googleapiclient.discovery import build


API_KEY: str = os.getenv('YT_API_KEY')
YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)


class Video:
    """
    Класс для ютуб-видео
    """
    def __init__(self, video_id: str) -> None:
        self.video = YOUTUBE.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                           id=video_id
                                           ).execute()
        self.video_id: str = video_id
        self.title: str = self.video['items'][0]['snippet']['title']
        self.url: str = f'https://www.youtube.com/watch?v={video_id}'
        self.view_count: int = self.video['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video['items'][0]['statistics']['likeCount']


    def __str__(self) -> str:
        """
        Информация об объекте для пользователей
        """
        return f'{self.title}'


class PLVideo(Video):
    """
    Класс для плейлистов ютуб
    """
    def __init__(self, video_id: str, playlist_id: str):
        self.playlist_videos = YOUTUBE.playlistItems().list(playlistId=playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        super().__init__(video_id)
        self.playlist_id = playlist_id
