import os
from datetime import timedelta


import isodate
from googleapiclient.discovery import build


class PlayList:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id):
        self.playlist_id = id
        request = self.youtube.playlists().list(part="snippet", id=self.playlist_id)
        response = request.execute()

        self.title = response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    @property
    def total_duration(self):
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails'
                                                            ).execute()

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        # print(video_ids)

        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()

        video_time = []
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            video_time.append(duration)
        total_durations = sum(video_time, timedelta())
        return total_durations

    def show_best_video(self):
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()
        vines_likes = {}
        for vine in video_response['items']:
            num_likes = vine['statistics']['likeCount']
            id_video = vine['id']
            vines_likes[int(num_likes)] = id_video
            max_num_likes = max(vines_likes.keys())
        return f"https://youtu.be/{vines_likes[max_num_likes]}"
