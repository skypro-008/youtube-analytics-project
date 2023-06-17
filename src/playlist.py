import os

import isodate
from googleapiclient.discovery import build
from datetime import timedelta
from src.utils import find_value
from src.youtube_object import YoutubeObject
from pprint import pprint


class PlayList(YoutubeObject):

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"
        self.__playlist_response = self.__get_playlist_response()

        self.title = find_value(self.__playlist_response, 'title')

        self.__playlist_videos = self.__get_playlist_videos()
        self.__video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__playlist_videos['items']]
        self.__video_response = self.__get_video_response()

        self.total_duration = self.__get_total_duration()

    def __get_playlist_response(self):
        playlist_response = PlayList.service.playlists().list(id=self.__playlist_id,
                                                              part='contentDetails, snippet',
                                                              maxResults=50,
                                                              ).execute()
        return playlist_response

    def __get_video_response(self):
        video_response = PlayList.service.videos().list(part='contentDetails,statistics',
                                                        id=','.join(self.__video_ids)
                                                        ).execute()

        # pprint(video_response)

        return video_response

    def __get_playlist_videos(self):
        playlist_videos = PlayList.service.playlistItems().list(playlistId=self.__playlist_id,
                                                                part='contentDetails',
                                                                maxResults=50,
                                                                ).execute()

        return playlist_videos

    def __get_total_duration(self):
        duration = timedelta(seconds=0)

        for video in self.__video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)

        return duration

    def show_best_video(self):
        def __like_count(video):
            return int(video['statistics']['likeCount'])

        most_liked_video = max(self.__video_response['items'], key=__like_count)

        return f"https://youtu.be/{most_liked_video['id']}"