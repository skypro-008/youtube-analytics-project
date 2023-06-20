from googleapiclient.discovery import build
import os


class Video:

    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    #api_key: str = os.getenv('YT_API_KEY')
    api_key: str = "AIzaSyBIE1Zoz-q-0QXM1H8hp3e_N9xnuT_9xfI"
    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        self.title = None
        self.url = None
        self.view_count = None
        self.like_count = None

        try:
            response = self.youtube.videos().list(
                part='snippet, statistics',
                id=self.video_id
            ).execute()
            video = response['items'][0]

            self.title = video['snippet']['title']
            self.url = "https://www.youtube.com/watch?v=" + self.video_id
            self.view_count = video['statistics']['viewCount']
            self.like_count = video['statistics']['likeCount']

        except Exception as e:
            print("Error:", str(e))

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
