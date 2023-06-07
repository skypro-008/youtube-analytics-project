import isodate
import datetime
import os
from googleapiclient.discovery import build


class YTMixin:
    """
    Класс-миксин для работы с API ютуба.
    """

    api_key: str = os.getenv('YT_API_KEY')

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с API youtube.
        """

        youtube = build('youtube', 'v3', developerKey=cls.api_key)

        return youtube


class PlayList(YTMixin):
    def __init__(self, playlist_id):

        self.playlist_id = playlist_id
        self.title = self.get_playlist_info()['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    def __repr__(self):
        return f"{self.__class__.__name__}, " \
               f"{self.playlist_id}," \
               f"{self.title}, " \
               f"{self.url}"

    def get_playlist_info(self):
        """
        Загружаем информацию о плейлисте
        """
        request = PlayList.get_service().playlists().list(part="snippet", id=self.playlist_id)
        response = request.execute()

        return response

    def get_video_response(self):
        """
        Получаем данные по видеороликам в плейлисте
        """
        playlist_videos = PlayList.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                                      part='contentDetails',
                                                                      maxResults=50).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = PlayList.get_service().videos().list(part='contentDetails,statistics',
                                                              id=','.join(video_ids)
                                                              ).execute()
        return video_response

    @property
    def total_duration(self):

        time_info = []

        for video in self.get_video_response()['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            time_info.append(duration)

        result = sum(time_info, datetime.timedelta())
        return result

    def show_best_video(self):
        """
        Находим и выводим ссылку на самое популярное видео из плейлиста (по количеству лайков)
        """

        top_result = 0
        top_url_video = ''

        for i in self.get_video_response()['items']:
            likes = i['statistics']['likeCount']
            if int(likes) > int(top_result):
                top_result = likes
                top_url_video = i['id']

        return f'https://youtu.be/{top_url_video}'
