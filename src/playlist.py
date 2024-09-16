import datetime

import isodate

from src.video import PLVideo
from src.video import Video


class PlayList(PLVideo):
    def __init__(self, plist_id):
        super().__init__('some_video_id', plist_id)
        self.plist_id = plist_id
        self.url = f"https://www.youtube.com/playlist?list={self.plist_id}"
        self.videos = []  # Инициализация списка видео

        # Получаем объект для работы с API
        super().get_service()

        # Получаем плейлист по его id
        self.playlist = self.get_service().playlists().list(id=self.plist_id, part='snippet').execute()
        self.title = self.playlist['items'][0]['snippet']['title']

        # Получаем список видео из плейлист
        self.playlist_videos = super().get_service().playlistItems().list(playlistId=self.plist_id,
                                                                          part='snippet,contentDetails',
                                                                          maxResults=50, ).execute()

        # Получаем все id видеоролика из playlist
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        # получаем информацию о видеороликах по списку собранных video_id
        self.video_response = super().get_service().videos().list(part='contentDetails,statistics',
                                                                  id=','.join(self.video_ids)
                                                                  ).execute()
        self.load_videos()

    def load_videos(self):
        for video_id in self.video_ids:
            video = Video(video_id)
            self.videos.append(video)

    @property
    def total_duration(self):
        # Получаем общую длительность видеороликов в плейлисте

        duration = datetime.timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)
        return duration

    def show_best_video(self):
        best_video = max(self.videos, key=lambda video: video.like_video)
        return f"https://youtu.be/{best_video.id_video}"