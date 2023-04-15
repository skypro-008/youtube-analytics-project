import os

from googleapiclient.discovery import build


class Video:
    """Класс Video"""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video):
        """
        Инициализация реальными данными следующих атрибутов экземпляра класса `Video`:
        id видео, название видео, ссылка на видео, количество просмотров, количество лайков
        """
        self.id_video = id_video
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=self.id_video).execute()
        self.title = self.video_response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v={self.id_video}'
        self.views_count = self.video_response['items'][0]['statistics']['viewCount']
        self.likes_count = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        """Метод `__str__`, возвращающий название видео"""
        return self.title


class PLVideo(Video):
    """Класс PLVideo - наследует класс Video"""
    def __init__(self, id_video, playlist_id):
        """
        Инициализация атрибутами класса Video с расширением
        атрибутом playlist_id
        """
        super().__init__(id_video)
        self.playlist_id = playlist_id
