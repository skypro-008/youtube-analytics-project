from src.baseclass import MixinBase
import datetime
import isodate


class PlayList(MixinBase):

    def __init__(self, playlist_id: str):
        """инициализация экземпляра класса"""
        self.__playlist_id = playlist_id
        # данные о плейлисте
        self.playlist_json = (
            self.get_service().playlists().list(id=self.__playlist_id, part='snippet').execute())
        self.title = self.playlist_json['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'
        # данные по видеороликам в плейлисте (id видеороликов, время публикации)
        self.playlist_videos = self.get_service().playlistItems().list(playlistId=playlist_id,
                                                                       part='contentDetails',
                                                                       maxResults=50,
                                                                       ).execute()
        # список всех id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        # данные видеороликов по их id из плейлиста (продолжительность, количество лайков и т.п.)
        self.video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                               id=','.join(video_ids)
                                                               ).execute()

    @property
    def total_duration(self):
        """возвращает длительность плейлиста"""
        total_duration = datetime.timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        max_likes = 0
        video_id = ''
        for video in self.video_response['items']:
            count_likes = int(video['statistics']['likeCount'])
            if max_likes < count_likes:
                max_likes = count_likes
                video_id = video['id']
        return f'https://youtu.be/{video_id}'