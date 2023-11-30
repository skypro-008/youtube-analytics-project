import os
import datetime
import isodate

from googleapiclient.discovery import build


class PlayList:
    api_key: str = os.getenv("YOU_API")
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.title = self.get_playlist_info()['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

    def __str__(self):
        return f'{self.title}'

    def get_playlist_info(self):
        """Функция возвращает информацию плэйлиста по id"""
        playlist_request = self.youtube.playlists().list(
            part="snippet",
            id=self.playlist_id
        ).execute()

        return playlist_request

    def get_playlist_id(self):
        """ Функция возвращает информиацию о видеороликах в плейлисте в виде списка """
        playlist_id = self.playlist_id
        playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        video_info: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_info

    @property
    def total_duration(self):
        """ Функция возвращает суммарную длительность видео плейлиста """
        list_of_duration = []
        videos_request = self.youtube.videos().list(part="contentDetails, statistics",
                                                    id=','.join(self.get_playlist_id())
                                                    ).execute()
        for video in videos_request['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            list_of_duration.append(duration)
        result = sum(list_of_duration, datetime.timedelta())
        return result

    def show_best_video(self):
        """ Функция возвращает ссылку на видео с максимальным колличеством лайков """
        max_like = 0
        best_video = ""
        for video in self.get_playlist_id():
            video_request = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                       id=video
                                                       ).execute()
            if int(video_request['items'][0]['statistics']['likeCount']) > max_like:
                max_like = int(video_request['items'][0]['statistics']['likeCount'])
                best_video = f"https://youtu.be/{video_request['items'][0]['id']}"
        return best_video

