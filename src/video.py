from googleapiclient.discovery import build
from config import yt_api_key


class Video:
    youtube = build('youtube', 'v3', developerKey=yt_api_key)

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.title = None
        self.video_url = None
        self.view_count = None
        self.like_count = None

        self.__update_attributes()

    def __str__(self):
        return self.title

    def __get_data(self) -> dict:
        return self.youtube.videos().list(part='snippet, statistics', id=self.video_id).execute()

    def __update_attributes(self) -> None:
        data = self.__get_data()
        self.title = data.get('items')[0].get('snippet').get('title')
        self.video_url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count = data.get('items')[0].get('statistics').get('viewCount')
        self.like_count = data.get('items')[0].get('statistics').get('likeCount')


class PLVideo(Video):
    def __init__(self, video_id: str, pl_id: str) -> None:
        super().__init__(video_id)
        self.pl_id = pl_id
