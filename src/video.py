"""Video and Play List Video class module"""
from googleapiclient.discovery import build  # pylint: disable=E0401

from src.constants import API_KEY


class Video:
    """
    Represents a YouTube video.

    Attributes:
        _video_id (str): The ID of the video.
        _video_title (str): The title of the video.
        _video_url (str): The URL of the video.
        _video_views (str): The number of views of the video.
        _video_likes (str): The number of likes on the video.
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
        self._video_title = self._snippet['title']
        self._video_url = youtube_url + video_id
        self._video_views = self._statistics['viewCount']
        self._video_likes = int(self._statistics['likeCount'])
        self._video_duration = self._content_details['duration']

    @property
    def _video_data(self) -> dict:
        """
        Retrieves the video data from the YouTube API.

        Returns:
            dict: The video data.
        """
        result: dict = self.__youtube.videos().list(
            part='snippet,statistics,contentDetails',
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

    @property
    def _content_details(self):
        """
        Returns the content details of the video.

        Returns:
            dict: A dictionary containing the content details of the video.
        """
        return self._video_data['contentDetails']

    @property
    def duration(self):
        """
        Returns the duration of the video.

        Returns:
            int: The duration of the video in seconds.
        """
        return self._video_duration

    @property
    def title(self):
        """
        Returns the title of the video.

        Returns:
            str: The title of the video.
        """
        return self._video_title

    @property
    def url(self):
        """
        Returns the URL of the video.

        Returns:
            str: The URL of the video.
        """
        return self._video_url

    @property
    def views(self):
        """
        Returns the number of views of the video.

        Returns:
            int: The number of views of the video.
        """
        return self._video_views

    @property
    def likes(self):
        """
        Returns the number of likes of the video.

        Returns:
            int: The number of likes of the video.
        """
        return self._video_likes

    def __str__(self) -> str:
        """
        Returns the string representation of the Video object.

        Returns:
            str: The title of the video.
        """
        return self._video_title

    def __repr__(self):
        """
        Return a string representation of the Video object.

        Returns:
            str: A string representation of the Video object.
        """
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
