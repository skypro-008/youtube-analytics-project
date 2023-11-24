import datetime
import isodate
import os
import requests

from googleapiclient.discovery import build


class PlayList:
    api_key = os.getenv('YouTube_ApiKey')
    url_pl = 'https://www.youtube.com/playlist?list='
    url_video = 'https://youtu.be/'

    def __init__(self, pl_id):
        self.__pl_id = pl_id
        self.title = self.channel_info()['items'][0]['snippet']['title']
        self.url = self.url_pl + self.__pl_id

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube

    @property
    def pl_id(self):
        return self.__pl_id

    def pl_response(self):
        """Метод для получения информации о плэйлисте"""
        pl_video = self.get_service().playlistItems().list(playlistId=self.__pl_id,
                                                           part='contentDetails',
                                                           maxResults=50,
                                                           ).execute()
        return pl_video

    @staticmethod
    def like_count(video_id):
        """Метод для получения количества лайков видео"""
        video = PlayList.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                     id=video_id
                                                     ).execute()
        likes = video['items'][0]['statistics']['likeCount']
        return int(likes)

    @property
    def total_duration(self):
        """Метод, который считает суммарную длительность плейлиста"""
        video_ids = [video['contentDetails']['videoId'] for video in self.pl_response()['items']]
        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                          id=','.join(video_ids)
                                                          ).execute()
        total_time = datetime.timedelta(0)
        for video in video_response['items']:
            iso_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_duration)
            total_time += duration
        return total_time

    def channel_info(self):
        """Метод для получения информации о канале по id плейлиста"""
        info = requests.get(
            f'https://www.googleapis.com/youtube/v3/playlists?key={self.api_key}&id={self.__pl_id}'
            f'&part=id,snippet&fields=items(id,snippet(title,channelId,channelTitle))')
        return info.json()

    def show_best_video(self):
        """Метод для получения ссылки на видео, с наибольшим количеством лайков"""
        id_video = ''
        best_likes = 0
        for video in self.pl_response()['items']:
            likes = self.like_count(video['contentDetails']['videoId'])
            if likes > best_likes:
                id_video = video['contentDetails']['videoId']
        return self.url_video + id_video
