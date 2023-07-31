import os
from googleapiclient.discovery import build


class Video:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        try:
            video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=self.video_id
                                                    ).execute()

            self.name = video_response['items'][0]['snippet']['title']
            self.url = f"https://www.youtube.com/watch?v={self.video_id}"
            self.comment_count = video_response['items'][0]['statistics']['commentCount']
            self.video_like_count = video_response['items'][0]['statistics']['likeCount']
            self.view_count = video_response['items'][0]['statistics']['viewCount']
        except Exception:
            print(f"Несуществующий id={video_id} видео")
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None


    def __str__(self):
        """
        Метод возвращающий название канала
        """
        return f"{self.name}"


class PLVideo(Video):
    """
    Класс инициализирует экземпляр по id видео и id плейлиста.
    """

    def __init__(self, video_id: str, id_playlist: str) -> None:
        super().__init__(video_id)
        self.id_playlist = id_playlist

    def __str__(self):
        return super().__str__()





