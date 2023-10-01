import os

from googleapiclient.discovery import build


class Video:
    __api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        self.video_response = Video.youtube.videos().list(
            part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.video_title = self.video_response['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.video_id}'
        self.view_count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        """
        Метод возвращает информацию об объекте для пользователя
        return: '<название канала>
        '"""
        return self.video_title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        """
        Экземпляр инициализируется id видео и id плейлиста.
        Данные будут подтягиваться из родительского класса Video.
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id
