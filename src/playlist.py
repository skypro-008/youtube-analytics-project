from src.constants import YOUTUBE
from datetime import timedelta
from src.video import Video


class PlayList:
    def __init__(self, playlist_id: str) -> None:
        self.playlist_id = playlist_id
        self.playlist = YOUTUBE.playlists().list(id=playlist_id,
                                                 part='snippet',
                                                 ).execute()
        self.playlist_videos = YOUTUBE.playlistItems().list(playlistId=playlist_id,
                                                             part='contentDetails',
                                                             ).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        self.videos = [Video(video['contentDetails']['videoId'])
                       for video in self.playlist_videos['items']]


    @property
    def total_duration(self):
        total_duration = timedelta(0)
        for video in self.videos:
            total_duration += video.duration
        return total_duration


    def show_best_video(self):
        best_video = self.videos[0]
        for video in self.videos:
            if video > best_video:
                best_video = video
        return best_video.url
