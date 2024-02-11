from src.channel import Channel
import os


class Video:
    """ Инициализируется реальными данными следующих атрибутов экземпляра класса"""
    api_key: str = os.getenv('YT_API_KEY')


    def __int__(self, video_id: str) -> None:
        self.video_id = video_id
        youtube = Channel.get_service()
        self.video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/{self.video_id}"
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']


    def __str__(self):
        return self.video_title

class PLVideo(Video):
    """Класс инициализируется  'id видео' и 'id плейлиста' """

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

