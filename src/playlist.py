import os

import isodate
from googleapiclient.discovery import build


class PlayList:

    def __init__(self, play_list_id):
        self.__api_key = os.getenv('API_KEY')
        self.__youtube = build('youtube', 'v3', developerKey=self.__api_key)
        self.play_list_id = play_list_id
        self.playlist_videos = self.__youtube.playlistItems().list(playlistId=self.play_list_id,
                                                                   part='contentDetails',
                                                                   maxResults=50,
                                                                   ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.__youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                           id=self.video_ids
                                                           ).execute()
        self.title = self.video_response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.play_list_id}'

    @property
    def total_duration(self):
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
        return duration

    @property
    def show_best_video(self):
        list_likes = {}
        list_id = []
        for i in self.video_ids:
            video_response_ = self.__youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                           id=i
                                                           ).execute()
            like_count = video_response_['items'][0]['statistics']['likeCount']
            list_likes[like_count] = i
            list_id.append(i)
        max_value = max(list_likes)
        indices = [index for index, val in enumerate(list_likes) if val == max_value]
        return f"https://youtu.be/{list_id[indices[0]]}"
