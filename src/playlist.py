import os
import json
from googleapiclient.discovery import build
import datetime
import isodate


class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.__api_key = os.getenv('YouTubeAPI')
        youtube = build('youtube', 'v3', developerKey=self.__api_key)

        playlists = youtube.playlistItems().list(playlistId=playlist_id,
                                               part='snippet',
                                               maxResults=50,).execute()

        self.title = playlists['items'][0]['snippet']['title'][:-13]
        self.url = f'https://www.youtube.com/playlist?list=' + self.playlist_id

    @property
    def total_duration(self):
        self.__api_key = os.getenv('YouTubeAPI')
        youtube = build('youtube', 'v3', developerKey=self.__api_key)
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        total_duration = datetime.timedelta()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration


    def show_best_video(self):

        self.__api_key = os.getenv('YouTubeAPI')
        youtube = build('youtube', 'v3', developerKey=self.__api_key)
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_ids).execute()
        video_likes = [{'video_id': video['id'], 'like_count': video['statistics']['likeCount']} for video in video_response['items']]

        sorted_videos = sorted(video_likes, key=lambda x: x['like_count'], reverse=True)

        most_popular_video_id = sorted_videos[0]['video_id']

        return f'https://youtu.be/{most_popular_video_id}'



# x = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
# print(x.show_best_video())