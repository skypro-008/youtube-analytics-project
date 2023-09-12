from src.channel import Channel
import datetime
import isodate


class PlayList(Channel):
    """
    Класс для плейлиста с ютуб-канала.
    Наследуется от класса ютуб-канала, чтобы не дублировать атрибуты и методы получения данных по API с ютуба.
    """
    def __init__(self, playlist_id: str) -> None:
        """Экземпляр инициализирует id плейлиста. Дальше все данные будут подтягиваться по API."""
        self.playlist_id = playlist_id
        # данные по play-листу канала
        self.playlist_dict = self.get_service().playlists().list(id=playlist_id, part='snippet').execute()
        self.title = self.playlist_dict['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
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
    def total_duration(self) -> datetime.timedelta:
        """
        Переводит продолжительность видео из формата ISO 8601 в объект класса `datetime.timedelta`
        и возвращает суммарную длительность плейлиста в виде объекта класса `datetime.timedelta`
        """
        total_duration = datetime.timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            # print(type(duration))  # <class 'datetime.timedelta'>
            total_duration += duration
        return total_duration

    def show_best_video(self) -> str:
        """Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        most_liked = 0
        video_id = ''
        for video in self.video_response['items']:
            likes_count = int(video['statistics']['likeCount'])
            if most_liked < likes_count:
                most_liked = likes_count
                video_id = video['id']
        return f'https://youtu.be/{video_id}'