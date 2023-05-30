"""Video and Play List Video class module"""
from googleapiclient.discovery import build  # pylint: disable=E0401

from src.constants import API_KEY


class Video:
    """
    Represents a YouTube video.

    Attributes:
        _video_id (str): The ID of the video.
        __video_title (str): The title of the video.
        __video_url (str): The URL of the video.
        __video_views (str): The number of views of the video.
        __video_likes (str): The number of likes on the video.
    """

    __youtube = build(
        'youtube',
        'v3',
        developerKey=API_KEY
    )

    def __init__(self, video_id: str):
        """
        Initializes a Video object.

        Args:
            video_id (str): The ID of the video.
        """
        youtube_url = 'https://www.youtube.com/watch?v='
        self._video_id = video_id
        self.__video_title = self._snippet['title']
        self.__video_url = youtube_url + video_id
        self.__video_views = self._statistics['viewCount']
        self.__video_likes = self._statistics['likeCount']

    def __str__(self) -> str:
        """
        Returns the string representation of the Video object.

        Returns:
            str: The title of the video.
        """
        return self.__video_title

    @property
    def _video_data(self) -> dict:
        """
        Retrieves the video data from the YouTube API.

        Returns:
            dict: The video data.
        """
        result: dict = self.__youtube.videos().list(
            part='snippet,statistics',
            id=self._video_id
        ).execute()
        return result['items'][0]

    @property
    def _snippet(self) -> dict:
        """
        Retrieves the snippet data of the video.

        Returns:
            dict: The snippet data of the video.
        """
        return self._video_data['snippet']

    @property
    def _statistics(self) -> dict:
        """
        Retrieves the statistics data of the video.

        Returns:
            dict: The statistics data of the video.
        """
        return self._video_data['statistics']

    def __repr__(self):
        return self._video_id


class PLVideo(Video):
    """
    Represents a video within a playlist.

    Inherits from the Video class.

    Attributes:
        playlist_id (str): The ID of the playlist.
    """

    def __init__(self, video_id: str, playlist_id: str):
        """
        Initializes a PLVideo object.

        Args:
            video_id (str): The ID of the video.
            playlist_id (str): The ID of the playlist.
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id
