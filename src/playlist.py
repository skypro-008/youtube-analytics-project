from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import isodate
import datetime

# Загружаем переменные из .env файла
load_dotenv()

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

class PlayList:
    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id
        self.playlist_data = self.get_playlist_data()
        self.title = self.playlist_data['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        self.videos = self.get_videos_in_playlist()

    def get_playlist_data(self):
        """Получает данные о плейлисте по его ID."""
        response = youtube.playlists().list(
            part='snippet',
            id=self.playlist_id
        ).execute()
        return response['items'][0]

    def get_videos_in_playlist(self):
        """Получает все видео в плейлисте."""
        video_ids = []
        next_page_token = None

        while True:
            response = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=self.playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            video_ids += [item['contentDetails']['videoId'] for item in response['items']]
            next_page_token = response.get('nextPageToken')

            if not next_page_token:
                break

        return video_ids

    @property
    def total_duration(self) -> datetime.timedelta:
        """Возвращает общую длительность плейлиста."""
        total_seconds = 0

        video_response = youtube.videos().list(
            part='contentDetails',
            id=','.join(self.videos)
        ).execute()

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_seconds += duration.total_seconds()

        return datetime.timedelta(seconds=total_seconds)

    def show_best_video(self) -> str:

        """Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)."""
        best_video_id = None
        max_likes = 0

        video_response = youtube.videos().list(
            part='statistics',
            id=','.join(self.videos)).execute()

        for video in video_response.get('items', []):
            like_count = int(video['statistics'].get('likeCount', 0))
            if like_count > max_likes:
                max_likes = like_count
                best_video_id = video['id']

        return f"https://youtu.be/{best_video_id}" if best_video_id else None

