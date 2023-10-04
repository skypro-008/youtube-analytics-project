import os

from googleapiclient.discovery import build

from src import InvalidIDError


class Video:
    __api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, video_id):
        try:
            self.video_id = video_id
            self.video_response = Video.youtube.videos().list(
                part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
            if not self.video_response['items']:
                raise InvalidIDError
        except InvalidIDError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        """
        Метод возвращает информацию об объекте для пользователя
        return: '<название канала>
        '"""
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        """
        Экземпляр инициализируется id видео и id плейлиста.
        Данные будут подтягиваться из родительского класса Video.
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id
