import os

from googleapiclient.discovery import build


class Video:

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        self.vid_title = self.get_video_info()['items'][0]['snippet']['title']
        self.vid_url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.vid_view_count = self.get_video_info()['items'][0]['statistics']['viewCount']
        self.vid_like_count = self.get_video_info()['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.vid_title}'

    def get_video_info(self):
        api_key: str = os.getenv("YOU_API")
        youtube = build('youtube', 'v3', developerKey=api_key)
        video_info = youtube.videos().list(part="snippet,statistics", id=self.video_id).execute()
        return video_info


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
