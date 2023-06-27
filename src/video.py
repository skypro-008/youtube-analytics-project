from googleapiclient.discovery import build
import os

class Video:
    def __init__(self, video_id: str) -> None:

        self.video_id = video_id #id видео
        self.video_title = self.get_video_response(video_id)['items'][0]['snippet']['title'] # название видео
        self.url = self.get_video_response(video_id)['items'][0]['snippet']['thumbnails']['default']['url']  # ссылка на видео
        self.view_count: int = self.get_video_response(video_id)['items'][0]['statistics']['viewCount']# количество просмотров
        self.like_count: int = self.get_video_response(video_id)['items'][0]['statistics']['likeCount']# количество лайков

    def __str__(self):
        return f"{self.video_title}"

    def api_key_youtube(self):
        api_key: str = os.getenv('YouTube_API')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def get_playlist(self,playlist_id):
        playlists = self.api_key_youtube().playlistItems().list(playlistId=playlist_id,
                                                 part='contentDetails',
                                                 maxResults=50,
                                                 ).execute()
        return  playlists

    def get_video_response(self,video_id):
        video_response = self.api_key_youtube().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        return  video_response


class PLVideo(Video):
    def __init__(self,video_id,playlist_id):
        super().__init__(video_id) #id видео
        self.playlist_id = self.get_playlist(playlist_id) # id плейлиста
        url = self.url  # ссылка на видео
        view_count = self.view_count # количество просмотров
        like_count = self.like_count # количество лайков


