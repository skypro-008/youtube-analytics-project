from googleapiclient.discovery import build
import os


class Video:
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str):
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=video_id
                                                    ).execute()
        self.__video_id = video_id
        self.__name = video_response['items'][0]['snippet']['title']
        self.__url = f"https://www.youtube.com/watch?v={self.__video_id}"
        self.__view_count = video_response['items'][0]['statistics']['viewCount']
        self.__likes_count = video_response['items'][0]['statistics']['likeCount']

    @property
    def video_id(self):
        return self.__video_id

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def view_count(self):
        return self.__view_count

    @property
    def likes_count(self):
        return self.__likes_count

    def __str__(self):
        return f"{self.__name}"


class PLVideo(Video):
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.__playlist_id = playlist_id

    def __str__(self):
        return f"{self.name}"
