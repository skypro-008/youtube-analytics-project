from src.youtube import youtube
from src.video import Video
from datetime import timedelta
import isodate
import json

class PlayList:

    def __init__(self, playlist_id: str):
        self.info = youtube.playlistItems().list(playlistId=playlist_id,
                                                 part='id,snippet,contentDetails',
                                                 fields='items(id,snippet(title,description,videoOwnerChannelId),'
                                                        'contentDetails(videoId))',
                                                 maxResults=50).execute()
        temp = youtube.playlists().list(channelId=self.info['items'][0]['snippet']['videoOwnerChannelId'],
                                        part='id,snippet',
                                        fields='items(id,snippet(title))',
                                        maxResults=50).execute()
        self.title = ''
        for item in temp['items']:
            if item['id'] == playlist_id:
                self.title = item['snippet']['title']
        temp = None

        self.id = playlist_id
        self.url ="https://www.youtube.com/playlist?list=" + self.id
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.info['items']]



    @property
    def total_duration(self) -> timedelta:
        video_list: list[object] = [Video(video_id).info for video_id in self.video_ids]
        d = timedelta(microseconds=0)
        for video in video_list:
            d += isodate.parse_duration(video['items'][0]['contentDetails']['duration'])
        return d

    def show_best_video(self) -> str:
        video_list: list[object] = [Video(video_id).info for video_id in self.video_ids]
        max_result = 0
        for video in video_list:
            result = int(video['items'][0]['statistics']['likeCount'])
            if result > max_result:
                max_result = result
                result_id = video['items'][0]['id']
        return f'https://youtu.be/{result_id}'
