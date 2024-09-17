import os
import isodate
import requests
import datetime
from googleapiclient.discovery import build


class PlayList:

    def __init__(self, id_playlist) -> None:
        self.id_playlist = id_playlist

        playlist_info = self.get_service().playlists().list(id=id_playlist,
                                                              part='contentDetails, snippet',
                                                              maxResults=50,
                                                              ).execute()

        self.title = playlist_info['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={id_playlist}"

        playlist_search = self.get_service().playlistItems().list(playlistId=id_playlist,
                                                              part='contentDetails, snippet',
                                                              maxResults=50,
                                                              ).execute()

        self.video_ids = [video['contentDetails']['videoId'] for video in playlist_search['items']]

    @property
    def total_duration(self):
        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                               id=','.join(self.video_ids)
                                               ).execute()
        duration_list = []

        duration_sum = datetime.timedelta(0, 0, 0, 0)

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            convert_duretion = isodate.parse_duration(iso_8601_duration)
            duration_list.append(convert_duretion)

        for duration in duration_list:
            duration_sum += duration   
        return duration_sum
    
    def show_best_video(self):
        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                               id=','.join(self.video_ids)
                                               ).execute()
        
        likes_amount = 0

        for video in video_response['items']:
            if int(video['statistics']['likeCount']) > int(likes_amount):
               likes_amount = video['statistics']['likeCount']
               video_link = f"https://youtu.be/{video['id']}"

        return video_link      

    @classmethod
    def get_service(cls):
        """
        Класс-метод
        :return: объект для работы с YouTube API
        """
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube
