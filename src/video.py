from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    def __init__(self, video_id: str):
        self.video_id = video_id
        self.title = None
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count = None
        self.like_count = None

        try:
            video_data = self.get_video_data()
            self.title = video_data['title']
            self.view_count = video_data['view_count']
            self.like_count = video_data['like_count']
        except Exception as e:
            print(f"Ошибка при получении данных о видео: {e}")


    def get_video_data(self):
        video_response = youtube.videos().list(
            part='snippet,statistics',
            id=self.video_id
        ).execute()

        video_info = video_response['items'][0]
        return {
            'title': video_info['snippet']['title'],
            'view_count': int(video_info['statistics']['viewCount']),
            'like_count': int(video_info['statistics']['likeCount'])
        }

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
