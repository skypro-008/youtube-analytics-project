import isodate
from datetime import datetime, time, timedelta

from src.channel import Channel
from src.video import Video


class PlayList:
    '''класс плейлистов
    param: title - название плейлиста
    param: url - ссылка на плейлист'''

    youtube = Channel.get_service()

    def __init__(self, playlist_id):

        playlist = self.youtube.playlists().list(id=playlist_id,
                                                 part='contentDetails,snippet',
                                                 maxResults=50,
                                                 ).execute()

        self.playlist_id = playlist_id
        self.title = playlist['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={playlist_id}'
        self.videos = []

    @property
    def videos(self):
        return self.__videos

    @videos.setter
    def videos(self, v):
        playlist_id = self.playlist_id
        playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()

        self.__videos: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

    @property
    def total_duration(self):
        playlist_id = self.playlist_id
        video_ids = self.videos

        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()
        duration = timedelta(hours=0, minutes=0)
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)
        return duration

    def show_best_video(self):
        tmp_dict = {}

        for id in self.__videos:
            video = Video(id)
            tmp_dict[id] = video.like_count
        sorted_dict = sorted(tmp_dict.items(), key=lambda item: item[1], reverse=True)
        return f'https://youtu.be/{sorted_dict[0][0]}'
