import os

from src.channel import Channel


class Video:
    def __init__(self, video_id):
        """Экземпляр инициализируется id видео.
        Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        self.object = Channel.get_service()
        self.info = self.object.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                              id=video_id
                                              ).execute()
        self.title = self.info['items'][0]['snippet']['title']
        self.url = os.path.join('https://www.youtube.com/watch?v=' + self.video_id)
        self.views = self.info['items'][0]['statistics']['viewCount']
        self.likes = self.info['items'][0]['statistics']['likeCount']
        self.duration = self.info['items'][0]['contentDetails']['duration']

    def __str__(self):
        """Возвращает инфо в формате '<название_видео>'"""
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, pl_id):
        """Дочерний класс от Video. Экземпляр инициализируется id видео и id плейлиста"""
        super().__init__(video_id)
        self.pl_id = pl_id
