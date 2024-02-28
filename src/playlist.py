import datetime
import isodate
from googleapiclient.discovery import build
import os

class PlayList:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')

    def __init__(self, playlists_id: str) -> None:
        """Экземпляр инициализируется id плейлиста. Дальше все данные будут подтягиваться по API."""
        self.playlists_id = playlists_id
        self.playlists_response = self.get_service().playlists().list(id=playlists_id,
                                               part='snippet').execute()
        self.title = self.playlists_response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlists_id}'

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=cls.api_key)

    @property
    def total_duration(self):
        """Возвращает объект класса datetime.timedelta с суммарной длительность плейлиста"""
        total = datetime.timedelta()
        playlist_videos = self.get_service().playlistItems().list(playlistId=self.playlists_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total += duration
        return total

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        best_video = ""
        playlist_videos = self.get_service().playlistItems().list(playlistId=self.playlists_id,
                                                       part='contentDetails',
                                                       maxResults=50,).execute()
        count_like = 0
        for video in playlist_videos['items']:

            video_id = video['contentDetails']['videoId']
            video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id).execute()
            like_count: int = video_response['items'][0]['statistics']['likeCount']
            if int(like_count) >= int(count_like):
                count_like = like_count
                best_video = f"https://youtu.be/{video_id}"
        return best_video

###############################################################