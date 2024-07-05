import os
import json
from googleapiclient.discovery import build

class Video:
    def __init__(self, id_video):

        self.id_video = id_video
        self.__api_key = os.getenv('YouTubeAPI')
        youtube = build('youtube', 'v3', developerKey=self.__api_key)

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=id_video
                                               ).execute()
        try:
            self.video_title = video_response['items'][0]['snippet']['title']
            self.video_url = f'https://www.youtube.com/watch?v={self.id_video}'
            self.video_view_count = video_response['items'][0]['statistics']['viewCount']
            self.video_likes_count = video_response['items'][0]['statistics']['likeCount']

        except IndexError:
            self.video_title = None
            self.video_url = None
            self.video_view_count = None
            self.video_likes_count = None



    def __str__(self):
        return f'{self.video_title}'

class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist
        self.__api_key = os.getenv('YouTubeAPI')
        youtube = build('youtube', 'v3', developerKey=self.__api_key)

        playlist_videos = youtube.playlistItems().list(playlistId=id_playlist,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()





# video1 = Video('AWX4JnAnjBE')
# print(video1.video_title)
# video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
# print(video2.video_title)