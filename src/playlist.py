import datetime
import os
from googleapiclient.discovery import build
import isodate


class PlayList:
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id: str):
        self.__playlist = self.youtube.playlists().list(id=playlist_id,
                                                        part='contentDetails, snippet',
                                                        ).execute()
        playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        self.__video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                           id=','.join(video_ids)
                                                           ).execute()
        self.id = playlist_id
        self.title = self.__playlist['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={playlist_id}'

    @property
    def total_duration(self):
        return sum([isodate.parse_duration(video['contentDetails']['duration'])
                    for video in self.__video_response['items']],
                   datetime.timedelta())

    def show_best_video(self):
        max_likes = int(self.__video_response['items'][0]['statistics']['likeCount'])
        best_video = f'https://www.youtube.com/watch?v={self.__video_response['items'][0]['id']}'
        for video in self.__video_response['items'][1:]:
            likes = int(video['statistics']['likeCount'])
            if max_likes < likes:
                max_likes = likes
                best_video = f'https://youtu.be/{video['id']}'

        return best_video
