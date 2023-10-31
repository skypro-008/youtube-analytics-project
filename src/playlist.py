import os
from googleapiclient.discovery import build
import datetime


class PlayList:
    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.__api_key = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.__api_key)
        self.playlist_info = self.youtube.playlists().list(id=self.__playlist_id,
                                                           part='snippet,contentDetails',
                                                           maxResults=50).execute()
        self.title = self.playlist_info['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"
        self.playlist_videos = self.youtube.playlistItems().list(
            playlistId=playlist_id, part='contentDetails',
            maxResults=50, ).execute()
        # получить все id видеороликов из плейлиста
        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(
            part='contentDetails,statistics', id=','.join(self.video_ids)).execute()

    @staticmethod
    def youtube_time_to_time_datatime(data_time):
        """
        Метод преобразования времени ролика из плейлиста
        в кортеж формата (часы, минуты, секунды)
        """
        h_ = 0
        m_ = 0
        s_ = 0
        num = ""
        for ch in data_time:
            if ch.isdigit():
                num += ch
            else:
                if ch.upper() == "H":
                    h_ = int(num)
                elif ch.upper() == "M":
                    m_ = int(num)
                elif ch.upper() == "S":
                    s_ = int(num)
                num = ""
        return h_, m_, s_

    @property
    def total_duration(self):
        time_data = datetime.timedelta(hours=0, minutes=0, seconds=0)
        for video in self.video_response['items']:
            time_var = self.youtube_time_to_time_datatime(video['contentDetails']['duration'])
            time_data = (time_data + datetime.timedelta(
                hours=time_var[0], minutes=time_var[1], seconds=time_var[2]))

        return time_data

    def show_best_video(self):
        max_like_count = int(self.video_response['items'][0]['statistics']['likeCount'])
        id_video_max_like = self.video_response['items'][0]['id']
        for video in self.video_response['items']:
            if int(video['statistics']['likeCount']) > max_like_count:
                max_like_count = int(video['statistics']['likeCount'])
                id_video_max_like = video['id']
        return f"https://youtu.be/{id_video_max_like}"
