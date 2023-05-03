import json
from googleapiclient.discovery import build
import os


class Video:
    """Класс для ютуб-видео"""

    api_key: str = os.getenv('API_KEY_YOU_TUBE')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_info: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.video_info = video_info
        self.video = self.youtube.videos().list(id=self.video_info, part='snippet,statistics').execute()
        self.video_id = self.video['items'][0]['id']
        self.video_title = self.video['items'][0]['snippet']['title']
        self.video_url = self.video['items'][0]['snippet']['thumbnails']['default']['url']
        self.video_number_views = self.video['items'][0]['statistics']['viewCount']
        self.video_number_like = self.video['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.video_title}'

    def to_json(self, dict_to_print) -> None:
        """Сохраняет в файл значения атрибутов экземпляра `Video`"""

        with open(dict_to_print, "w", encoding='utf-8') as write_file:
            json.dump({"id": self.video_id,
                       "title": self.video_title,
                       "url": self.video_url,
                       "likeCount": self.video_number_like,
                       "viewCount": self.video_number_views}, write_file, indent=2, ensure_ascii=False, separators=(',', ': '))
            print(dict_to_print)


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
