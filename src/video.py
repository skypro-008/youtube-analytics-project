from src.youtube import youtube
import json


class Video:
    """
    Класс для работы с видосиками
    """
    def __init__(self, video_id: str):
        self.id = None
        self.title = None
        self.url = None
        self.view_count = None
        self.like_count = None
        try:
            self.info = youtube.videos().list(part='id,snippet,contentDetails,statistics',
                                          fields='items(id, snippet(title), '
                                                 'contentDetails(duration), '
                                                 'statistics(viewCount,likeCount))',
                                          id=video_id).execute()
            self.id = video_id
            self.title = self.info['items'][0]['snippet']['title']
            self.url = "https://youtu.be/" + self.id
            self.view_count = self.info['items'][0]['statistics']['viewCount']
            self.like_count = self.info['items'][0]['statistics']['likeCount']
        except:
            self.id = video_id

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    """
    Класс для работы с видосиками в плейлистах
    """
    def __init__(self, video_id: str, playlist_id: str):
        self.list_id = None
        self.url = None
        super().__init__(video_id)
        if not self.title:
            self.list_id = playlist_id
            self.url = "https://youtu.be/" + video_id + '?list=' + self.list_id
