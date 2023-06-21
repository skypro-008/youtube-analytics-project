import datetime
import os
from googleapiclient.discovery import build

import isodate


class PlayList:
    API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist_response = self.youtube.playlists().list(part='snippet', id=playlist_id).execute()
        self.title = self.playlist_response["items"][0]["snippet"]["title"]
        self.url = "https://www.youtube.com/playlist?list=" + self.playlist_id
        self.__total_duration = None

    @property
    def total_duration(self):
        """
        Возвращает объект класса `datetime.timedelta` с суммарной
        длительность плейлиста.(обращение как к свойству, использовать @property)
        """
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()
        total_time = datetime.timedelta()

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_time += duration
        return total_time

    def show_best_video(self):
        """
        Возвращаем ссылку на самое популярное видео из плейлиста (по
        количеству лайков).
        """
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        best_like = {}
        for i in video_ids:
            video = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=i).execute()
            like = (video['items'][0]['statistics']['likeCount'])
            best_like[i] = int(like)
            max_val_key = max(best_like, key=best_like.get)

        return f'https://youtu.be/{max_val_key}'
