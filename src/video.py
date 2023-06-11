from src.playlist import YTMixin


class Video(YTMixin):
    """Класс для ютуб-канала"""

    def __init__(self, video_id):
        self.video_id = video_id
        try:

            video_response = Video.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                               id=video_id
                                                               ).execute()
            self.video_title: str = video_response['items'][0]['snippet']['title']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']
            self.comment_count: int = video_response['items'][0]['statistics']['commentCount']

        except IndexError:
            self.video_title = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None

    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
