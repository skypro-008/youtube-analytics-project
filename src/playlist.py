import datetime
import isodate
from src.channel import Channel


class PlayList:
    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id
        self.url = "https://www.youtube.com/playlist?list=" + self.playlist_id
        self.playlist_videos = Channel.get_service().playlistItems().list(
                                        playlistId=self.playlist_id,
                                        part='contentDetails, snippet',
                                        maxResults=50,
                                        ).execute()
        self.channel_id = self.playlist_videos['items'][0]['snippet']['channelId']
        self.playlists = Channel.get_service().playlists().list(
                                        channelId=self.channel_id,
                                        part='contentDetails,snippet',
                                        maxResults=50,
                                        ).execute()
        for playlist in self.playlists['items']:
            if playlist['id'] == self.playlist_id:
                self.title = playlist['snippet']['title']
                break

    def videos_info(self):
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        video_response = Channel.get_service().videos().list(
                            part='contentDetails,statistics',
                            id=','.join(video_ids)
        ).execute()
        return video_response

    @property
    def total_duration(self):
        all_time = datetime.timedelta(seconds=0)
        for video in self.videos_info()['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            all_time += duration
        return all_time

    def show_best_video(self):
        time_list = []
        url_list = []
        for video in self.videos_info()['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration).seconds
            time_list.append(duration)
            url_list.append(video['id'])
        best_video = "https://youtu.be/" + url_list[time_list.index(max(time_list))]
        return best_video
