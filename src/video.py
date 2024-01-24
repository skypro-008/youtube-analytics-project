from src.youtube import youtube


class Video:
    """
    Класс для работы с видосиками
    """
    def __init__(self, video_id: str):
        self.info = youtube.videos().list(part='snippet,statistics', id=video_id).execute()
        self.id = video_id
        self.title = self.info['items'][0]['snippet']['title']
        self.url = "https://youtu.be/" + self.id
        self.view_count = self.info['items'][0]['statistics']['viewCount']
        self.like_count = self.info['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    """
    Класс для работы с видосиками в плейлистах
    """
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.list_id = playlist_id
        self.url = "https://youtu.be/" + video_id + '?list=' + self.list_id
