import os
from googleapiclient.discovery import build


class Video:
    """Класс по видео из ютуба"""

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.request = (
            self.get_service()
            .videos()
            .list(part="snippet,contentDetails,statistics", id=self.video_id)
        )
        self.response = self.request.execute()
        self.name = self.response["items"][0]["snippet"]["title"]
        self.url = f"https://www.youtube.com/channel/{self.video_id}"
        self.view_count = self.response["items"][0]["statistics"]["viewCount"]
        self.like_count = self.response["items"][0]["statistics"]["likeCount"]

    @classmethod
    def get_service(cls) -> build:
        """
        Класс-метод, возвращающий объект для работы с YouTube API
        """
        channel_id = os.getenv("YT_API_KEY")
        cls.youtube = build("youtube", "v3", developerKey=channel_id)
        return build("youtube", "v3", developerKey=channel_id)

    def __str__(self):
        """
        Возвращет названия видео
        """
        return f"{self.name}"


class PLVideo(Video):
    """Класс для видео по плейлисту из ютуб-канала"""

    def __init__(self, id_video: str, id_playlist: str):
        super().__init__(id_video)
        self.id_playlist = id_playlist
        self.playlist_videos = (
            self.get_service()
            .playlistItems()
            .list(
                playlistId=self.id_playlist,
                part="contentDetails",
                maxResults=50,
            )
            .execute()
        )

    def __str__(self):
        """
        Возвращет названия видео
        """
        return f"{self.name}"
