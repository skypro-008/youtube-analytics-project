import os
import datetime

import isodate
from googleapiclient.discovery import build
from functools import total_ordering

api_key: str = os.getenv('YT_API_KEY')
class PlayList:

    service = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id



        response = PlayList.service.playlists().list(id=self.playlist_id,
                                                    part='contentDetails,snippet',
                                                    maxResults=50,
                                                    ).execute()

        self.title: str = response['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.playlist_id
        self.total_duration = self.get_total_duration()

    def __eq__(self, other):
        return

    def get_total_duration(self):
        playlist_videos = PlayList.service.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()


        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        # print(video_ids)

        '''
        вывести длительности видеороликов из плейлиста
        docs: https://developers.google.com/youtube/v3/docs/videos/list
        '''
        video_response = PlayList.service.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        # printj(video_response)
        total_duration = datetime.timedelta()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            total_duration += isodate.parse_duration(iso_8601_duration)
        return total_duration

    def show_best_video(self):
        playlist_videos = PlayList.service.playlistItems().list(playlistId=self.playlist_id,
                                                                part='contentDetails',
                                                                maxResults=50,
                                                                ).execute()

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        # print(video_ids)

        '''
        вывести длительности видеороликов из плейлиста
        docs: https://developers.google.com/youtube/v3/docs/videos/list
        '''
        video_response = PlayList.service.videos().list(part='contentDetails,statistics',
                                                        id=','.join(video_ids)
                                                        ).execute()

        most_liked_video = max(video_response['items'], key=lambda x: int(x['statistics']['likeCount']))
        return f"https://youtu.be/{most_liked_video['id']}"

# pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
# print(pl.title)
# print(pl.url)
