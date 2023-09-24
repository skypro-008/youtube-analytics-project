from src.get_service import *
import datetime
import isodate

@dataclass
class PlayList(Get_Service):
    playlist_id: str

    def __post_init__(self):
        self.PLAYLIST_INFO = self.youtube.playlists().list(id=self.playlist_id, part='snippet, contentDetails').execute()
        self.title: str = self.PLAYLIST_INFO['items'][0]['snippet']['title']
        self.url: str = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    def VIDEO_LIST_INFO(self):
        """Возвращает информацию о всех видео в плейлисте"""
        self.PLAYLIST_ITEMS_INFO = self.youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails').execute()
        self.video_id = [video['contentDetails']['videoId'] for video in self.PLAYLIST_ITEMS_INFO['items']]
        self.VIDEO_INFO = self.youtube.videos().list(id=','.join(self.video_id), part='contentDetails,statistics').execute()
        return self.VIDEO_INFO

    @property
    def total_duration(self):
        """Возвращает объект класса `datetime.timedelta` с суммарной длительностью плейлиста."""
        total_duration = datetime.timedelta()
        for video in self.VIDEO_LIST_INFO()['items']:
            duration = isodate.parse_duration(video['contentDetails']['duration'])
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео в плейлисте."""
        video_likes = []
        for likes in self.VIDEO_LIST_INFO()['items']:
            video_likes.append(likes['statistics']['likeCount'])
        return f"https://youtu.be/{self.video_id[video_likes.index(max(video_likes))]}"