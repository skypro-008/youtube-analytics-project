import requests
from googleapiclient.discovery import build

from src.config import get_api_key


class Video:
    """Класс для ютуб-видео"""
    api_key = get_api_key()
    """Экземпляр инициализирует id канал. Дальше все данные будут подтягиваться по API."""
    def __init__(self, id_video):
        self.id_video = id_video
        self.name_video = ""
        self.url_video = ""
        self.view_video = None
        self.like_video = None

        self.request = self.get_service().videos().list(
            part="snippet,statistics",
            id=self.id_video
        )

        response = self.request.execute()

        if response['items']:
            video_data = response['items'][0]
            self.name_video = video_data['snippet']['title']
            self.url = f"https://www.youtube.com/watch?v={self.id_video}"
            self.view_video = int(video_data['statistics']['viewCount'])
            self.like_video = int(video_data['statistics']['likeCount'])


    def get_service(self):
        return build("youtube", "v3", developerKey=self.api_key)


    def __str__(self):
        return self.name_video


class PLVideo:
    """Класс для  'id видео' и 'id плейлиста'"""
    api_key = get_api_key()

    def __init__(self, video_id, playlist_id):
        video_info = self.get_video_info(video_id)
        playlist_info = self.get_playlist_info(playlist_id)

        if 'items' in video_info:
            video_data = video_info['items'][0]['snippet']
            self.name_video = video_data['title']
            self.url = f"https://www.youtube.com/watch?v={video_id}"
        else:
            self.name_video = "Video not found"


    def get_video_info(self, video_id):
        url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={self.api_key}&part=snippet,statistics'
        response = requests.get(url)
        video_info = response.json()
        return video_info


    def get_playlist_info(self, playlist_id):
        url = f'https://www.googleapis.com/youtube/v3/playlists?id={playlist_id}&key={self.api_key}&part=snippet'
        response = requests.get(url)
        playlist_info = response.json()
        return playlist_info


    def __str__(self):
        return self.name_video