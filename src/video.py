from src.channel import *


class Video:
    """Класс для видео"""
    YT_API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=YT_API_KEY)

    def __init__(self, video_id: str):
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        VIDEO_INFO = self.youtube.videos().list(id=video_id, part='snippet,statistics').execute()
        self.title: str = VIDEO_INFO['items'][0]['snippet']['title']
        self.url: str = f'https://www.youtube.com/watch?v={video_id}'
        self.view_count: int = VIDEO_INFO['items'][0]['statistics']['viewCount']
        self.like_count: int = VIDEO_INFO['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id
