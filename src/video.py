from src.channel import Channel


class Video:
    """ класс видео"""
    youtube = Channel.get_service()

    def __init__(self, video_id: str):
        """конструктор экземпляра
        param video_id - id видео ролика"""
        try:
            self.info = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id).execute()
            self.video_id = video_id
            self.title = self.info['items'][0]['snippet']['title']
            self.url = f'https://www.youtube.com/watch?v={video_id}'
            self.view_count = int(self.info['items'][0]['statistics']['viewCount'])
            self.like_count = int(self.info['items'][0]['statistics']['likeCount'])
            self.comment_count = int(self.info['items'][0]['statistics']['commentCount'])
        except IndexError:
            self.info = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id).execute()
            self.video_id = video_id
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    """Подкласс видео с плейлистом"""

    def __init__(self, video_id, playlist_id):
        """конструктор экземпляра
        param video_id - id видео ролика
        param playlist_id - id плейлиста"""

        super().__init__(video_id)
        self.playlist_id = playlist_id
